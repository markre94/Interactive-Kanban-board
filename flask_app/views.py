from  flask_app import app,db
from flask import redirect,render_template,url_for,flash,request
from flask_app.models import Task
from flask_app.forms import RegistrationFrom, LoginFrom


@app.route('/')
def home():
    return render_template('base.html')


@app.route('/app', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        try:
            task_content = request.form ['content']
            if task_content == '':
                flash('The task must contain something.', 'warning')
                return redirect('/app')
            else:
                new_task = Task(content=task_content, status='to_do')

                try:
                    db.session.add(new_task)
                    db.session.commit()
                    return redirect('/app')
                except:
                    return 'There was an issue adding your task'
        except:
            flash("Ups forgot to add file")
    else:
        tasks = Task.query.order_by(Task.date_created).all()

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