from flask_app import app, db, bcrypt
from flask import redirect, render_template, flash, request, url_for
from flask_app.models import Task, User
from flask_app.forms import RegistrationFrom, LoginFrom
from flask_login import login_user, current_user, logout_user, login_required



@app.route('/')
def home():
    return render_template('base.html')


@app.route('/app', methods=['POST', 'GET'])
@login_required
def index():
    if request.method == 'POST':
        try:
            task_content = request.form ['content']
            if task_content == '':
                flash('The task must contain something.', 'warning')
                return redirect('/app')
            else:
                new_task = Task(content=task_content, status='to_do', owner=current_user)

                try:
                    db.session.add(new_task)
                    db.session.commit()
                    return redirect('/app')
                except:
                    return 'There was an issue adding your task'
        except:
            flash("Ups forgot to add file")
    else:
        tasks = current_user.tasks

        return render_template('main.html', tasks=tasks)


@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Task.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/app')
    except:
        return "There was an problem "


@app.route('/task/<status>/<int:id>')
def take_task(status, id):
    task_to_take = Task.query.get_or_404(id, status)
    try:
        if task_to_take.status == "to_do":
            task_to_take.status = "doing"
            db.session.commit()
            return redirect('/app')
        elif task_to_take.status == "doing":
            task_to_take.status = "done"
            db.session.commit()
            return redirect('/app')
        else:
            task_to_take.status = "done"
            db.session.commit()
            return redirect('/app')
    except:
        return "There was an problem "


@app.route('/discard/<int:id>')
def discard(id):
    task_to_take = Task.query.get_or_404(id)
    try:
        task_to_take.status = "to_do"
        db.session.commit()
        return redirect('/app')
    except:
        return "There was an problem "


@app.route('/login', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        flash('You are already logged in', 'success')
        return redirect(url_for('home'))
    form = LoginFrom()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash("Login unsuccessful", "danger")
    return render_template(template_name_or_list='login.html', form=form, title="Login")


@app.route('/register', methods=['POST', 'GET'])
def register():
    if current_user.is_authenticated:
        flash('You are already logged in', 'success')
        return redirect(url_for('home'))
    form = RegistrationFrom()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f"Your account has been created! Your are now able to log in!", 'success')
        return redirect(url_for('login'))
    return render_template(template_name_or_list='sign_in.html', form=form, title="Register")


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/log')
def log():
    return render_template('log.html')


@app.route('/dashboard')
@login_required
def account_dashboard():
    return render_template('user_dash.html', title='Dashboard')



