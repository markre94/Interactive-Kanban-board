from flask import Flask, render_template, url_for, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from sqlalchemy import Enum

app = Flask('__name__')
app.config ["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class Task(db.Model) :
    """Task class
    Attributes:
        id (int): Unique id, primary key, auto increment.
        username (str): Foreign key referencing Users table.
        task (str): Details of the task.
        status (enum): Status of the task, with the following values
            - 'to_do'
            - 'doing'
            - 'done'
    """

    id = db.Column(db.Integer, primary_key=True)
    # username = db.Column(db.String, db.ForeignKey('users.username'))
    content = db.Column(db.String, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(Enum('to_do', 'doing', 'done'))


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST' :
        task_content = request.form ['content']
        if task_content == '' :
            flash('The task must contain something.', 'error')
            return redirect('/')
        else :
            new_task = Task(content=task_content, status='to_do')

            try :
                db.session.add(new_task)
                db.session.commit()
                return redirect('')
            except :
                return 'There was an issue adding your task'

    else :
        tasks = Task.query.order_by(Task.date_created).all()

        return render_template('main.html', tasks=tasks)

@app.route('/delete')
def delete():
    pass

if __name__ == "__main__" :
    app.run(debug=True)
