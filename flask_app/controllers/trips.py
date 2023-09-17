from flask_app import app 
from flask_app.models import trip
from flask_app.models import user
from flask import render_template, redirect, request, session, jsonify, send_from_directory
import os

@app.route('/explore') 
def show_all():
    if 'user_id' not in session:
        return redirect('/')
    all_trips = trip.Trip.get_all() 
    user_saved_trips = user.User.get_saved_trips(session['user_id'])
    saved_trips_ids = []
    for one_trip in user_saved_trips.saved_trips: 
        saved_trips_ids.append(one_trip.id)

    user_trips = user.User.get_my_trips(session['user_id'])
    my_trips_ids = []
    for one_trip in user_trips.trips:
        my_trips_ids.append(one_trip.id)

    return render_template("explore.html", all_trips=all_trips, saved_trips_ids=saved_trips_ids, my_trips_ids=my_trips_ids, user_id=session['user_id'])

@app.route("/uploads/<filename>")
def serve_uploads(filename):
    if 'user_id' not in session:
        return redirect('/')
    return send_from_directory(app.config["UPLOAD_DIR"], filename)

@app.route('/create')
def create_page():
    if 'user_id' not in session:
        return redirect('/')
    create_data = session.pop('create_data', None)
    one_user = user.User.get_one(session['user_id'])
    return render_template('create_trip.html', user=one_user, create_data=create_data)

@app.route('/create_itinerary', methods=['POST'])
def create_itinerary():
    if not trip.Trip.validate_trip(request.form, request.files['cover_photo']):
        session['create_data'] = request.form
        return redirect('/create')
    trip_id = trip.Trip.save(request.form, request.files['cover_photo'], session['user_id'])
    session.pop('create_data', None)
    return redirect(f'/add_days/{trip_id}')
    
@app.route('/view/<int:trip_id>')
def view(trip_id):
    if 'user_id' not in session:
        return redirect('/')
    one_trip = trip.Trip.get_one(trip_id)

    user_saved_trips = user.User.get_saved_trips(session['user_id'])
    saved_trips_ids = []
    for a_trip in user_saved_trips.saved_trips: 
        saved_trips_ids.append(a_trip.id)

    user_trips = user.User.get_my_trips(session['user_id'])
    my_trips_ids = []
    for a_trip in user_trips.trips:
        my_trips_ids.append(a_trip.id)

    api_key = os.environ.get('FLASK_APP_API_KEY')
    coordinates = trip.Trip.get_coordinates(trip_id)
    return render_template("view.html", trip=one_trip, saved_trips_ids=saved_trips_ids, my_trips_ids=my_trips_ids, user_id = session['user_id'], api_key=api_key, coordinates=coordinates)

@app.route('/edit_trip/<int:trip_id>')
def edit_trip_page(trip_id):
    if 'user_id' not in session:
        return redirect('/')
    one_user = user.User.get_one(session['user_id'])
    one_trip = trip.Trip.get_one(trip_id)
    return render_template("edit_trip.html", trip=one_trip, user=one_user)

@app.route('/edit_trip/<int:trip_id>', methods=['POST'])
def edit_trip(trip_id):
    if not trip.Trip.validate_trip(request.form, request.files['cover_photo']):
        return redirect(f'/edit_trip/{trip_id}')
    trip.Trip.edit(trip_id, request.files['cover_photo'], request.form)
    return redirect(f'/edit_days/{trip_id}')

@app.route('/save_coordinates/<int:trip_id>', methods=['POST'])
def save_coordinates(trip_id):
    if 'user_id' not in session:
        return redirect('/')
    trip.Trip.save_coordinates(request.form, trip_id)
    return jsonify({"message": "Map Coordinates Saved"})

@app.route('/delete/<int:trip_id>')
def delete_trip(trip_id):
    if 'user_id' not in session:
        return redirect('/')
    trip.Trip.delete(trip_id)
    return redirect('/profile')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')