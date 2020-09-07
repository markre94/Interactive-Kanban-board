from flask import redirect,render_template,url_for,flash,request
from flask_app.models import Task
from flask_app.forms import RegistrationFrom, LoginFrom
from flask_app import app


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
        flash(f"User created for {form.username.data}!", 'success')
        return redirect(url_for('index'))
    return render_template(template_name_or_list='sign_in.html', form=form, title="Register")
