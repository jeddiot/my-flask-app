from myproject import app, db
from flask import render_template, redirect, request, url_for, flash, abort
from flask_login import login_user, login_required, logout_user
from myproject.models import User
from myproject.forms import LoginForm, RegistrationForm

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/welcome')
@login_required # return to login page if not logged in
def welcome_user():
    return render_template('welcome_user.html')

@app.route('/logout')
@login_required # return to login page if not logged in
def logout():
    logout_user()
    flash("You're logged out.")
    return redirect(url_for('home'))

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()

        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash('Logged in successfully.')
            next = request.args.get('next') # the page the user was visiting before logged in

            if next == None or next[0] == '/':
                next = url_for('welcome_user')
            
            return redirect(next)
    return render_template('login.html', form = form)

@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data,
                    username = form.username.data,
                    password = form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Thanks for registration, your UserName passed the 3 requirements!")
        return redirect(url_for('login'))
    return render_template('register.html', form = form)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

if __name__ == '__main__':
    app.run(debug = True)