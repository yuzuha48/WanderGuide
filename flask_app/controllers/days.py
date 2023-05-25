from flask_app import app 
from flask_app.models import day
from flask_app.models import trip
from flask_app.models import user
from flask import render_template, redirect, request, session, flash, jsonify
import os

@app.route('/add_days/<int:trip_id>')
def days_page(trip_id):
    if 'user_id' not in session:
        return redirect('/')
    day_data = session.pop('day_data', None)
    one_trip = trip.Trip.get_one(trip_id)
    api_key = os.environ.get('FLASK_APP_API_KEY')
    return render_template("create_days.html", trip_id=trip_id, city=one_trip.city, api_key=api_key)

@app.route('/add_days/<int:trip_id>', methods=['POST'])
def create_days(trip_id):
    if len(request.form) < 1:
        return jsonify({"message": "Error"})

    for form_key in request.form.keys():
        print("start of print ---------------------")
        print(request.form[form_key][2])
        print("end of print ---------------------")
        if not day.Day.validate_day(request.form[form_key]):
            session['day_data'] = request.form
            return jsonify({"message": "Error"})

    for form_key in request.form.keys():
        day.Day.save(request.form[form_key], trip_id)
        session.pop('day_data', None)
    return jsonify({"message": "Day Added"})

@app.route('/edit_days/<int:trip_id>')
def edit_days_page(trip_id):
    if 'user_id' not in session:
        return redirect('/')
    one_user = user.User.get_one(session['user_id'])
    one_trip = trip.Trip.get_one(trip_id)
    api_key = os.environ.get('FLASK_APP_API_KEY')
    coordinates = trip.Trip.get_coordinates(trip_id)
    return render_template("edit_days.html", trip=one_trip, user=one_user, api_key=api_key, coordinates=coordinates)

@app.route('/edit_days/<int:day_id>', methods=['POST'])
def edit_days(day_id):
    if not day.Day.validate_day(request.form):
        session['day_data'] = request.form
        return jsonify({"message": "Error"})
    day.Day.edit(day_id, request.form)
    session.pop('day_data', None)
    return jsonify({"message": "Updated"})