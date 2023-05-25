from flask_app import app 
from flask import render_template, redirect, request, session, flash, jsonify
from flask_app.models import user
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def reroute():
    return redirect('/login')

@app.route('/login')
def login_page():
    return render_template("login.html")

@app.route('/login', methods=['POST'])
def login():
    user_in_db = user.User.get_by_email(request.form)
    if not user_in_db:
        session["login_email"] = request.form["email"]
        flash("Invalid Email.", "login")
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        session["login_email"] = request.form["email"]
        flash("Invalid Password.", "login")
        return redirect('/')
    session['user_id'] = user_in_db.id
    return redirect('/explore')

@app.route('/register')
def registration_page():
    form_data = session.pop('form_data', None)
    return render_template("register.html", form_data=form_data)

@app.route('/register', methods=['POST'])
def register():
    if not user.User.validate_user(request.form):
        session["form_data"] = request.form
        return redirect('/register')

    user_id = user.User.save(request.form)
    session["user_id"] = user_id
    session.pop('form_data', None)
    return redirect('/explore')

@app.route('/profile')
def profile():
    if 'user_id' not in session:
        return redirect('/')
    user_trips = user.User.get_my_trips(session['user_id'])
    user_saved_trips = user.User.get_saved_trips(session['user_id'])
    return render_template("profile.html", user=user_trips, one_user=user_saved_trips)
    
@app.route('/save/<int:trip_id>')
def save(trip_id):
    if 'user_id' not in session:
        return redirect('/')
    user.User.save_trip(session['user_id'], trip_id)
    return jsonify({"message": "Saved"})

@app.route('/unsave/<int:trip_id>')
def unsave(trip_id):
    if 'user_id' not in session:
        return redirect('/')
    user.User.unsave_trip(session['user_id'], trip_id)
    return jsonify({"message": "Unsaved"})