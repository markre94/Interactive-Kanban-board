from flask import redirect, render_template, url_for, flash, request
from flask_app.models import Task, User
from flask_app.forms import RegistrationFrom, LoginFrom
from flask_app import app, bcrypt, db


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginFrom()
    if form.validate_on_submit():
        if form.email.data == 'markre94@icloud.com' and form.password.data == "elo":
            flash(f'You are now logged in as {form.email.data}!', 'success')
            return redirect(url_for('index'))
        else:
            flash("Login unsuccessful", "danger")
    return render_template(template_name_or_list='login.html', form=form, title="Login")


@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegistrationFrom()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f"Your account has been created! Your are now able to log in!", 'success')
        return redirect(url_for('login'))
    return render_template(template_name_or_list='sign_in.html', form=form, title="Register")
