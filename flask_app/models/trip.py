from flask import flash
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user 
from flask_app.models import day 
import uuid
import os

class Trip:
    DB = "trips_schema"
    def __init__(self, data):
        self.id = data["id"]
        self.country = data["country"]
        self.city = data["city"]
        self.length_of_stay = data["length_of_stay"]
        self.cover_photo = data["cover_photo"]
        self.itinerary_description = data["itinerary_description"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user = None
        self.days = []
        self.saved_by = None

    @classmethod
    def get_one(cls, trip_id):
        data = {"id": trip_id}
        query = """
                SELECT * FROM trips 
                LEFT JOIN days ON days.trips_id = trips.id
                JOIN users ON users.id = trips.users_id
                WHERE trips.id=%(id)s;
                """
        results = connectToMySQL(cls.DB).query_db(query, data)
        one_trip = cls(results[0])
        for row in results:
            user_data = {
                "id": row["users.id"],
                "first_name": row["first_name"], 
                "last_name": row["last_name"], 
                "email": row["email"], 
                "password": row["password"], 
                "created_at": row["users.created_at"], 
                "updated_at": row["users.updated_at"]
            }
            if row["days.id"]:
                day_data = {
                    "id": row["days.id"],
                    "day_theme": row["day_theme"],
                    "location": row["location"],
                    "activity": row["activity"],
                    "created_at": row["days.created_at"],
                    "updated_at": row["days.updated_at"],
                }
                one_trip.days.append(day.Day(day_data))
        one_trip.user = user.User(user_data)
        one_trip.saved_by = Trip.get_saved_by(trip_id)
        return one_trip

    @classmethod
    def get_all(cls):
        query = """ SELECT * FROM trips 
                JOIN users ON users.id = trips.users_id
                """
        results = connectToMySQL(cls.DB).query_db(query)
        all_trips = []
        if results:
            for row in results:
                one_trip = cls(row)
                user_data = {
                    "id": row['users.id'], 
                    "first_name": row['first_name'],
                    "last_name": row['last_name'],
                    "email": row['email'],
                    "password": row['password'],
                    "created_at": row['users.created_at'],
                    "updated_at": row['users.updated_at']
                }   
                one_trip.user = user.User(user_data)
                one_trip.saved_by = Trip.get_saved_by(row["id"])
                all_trips.append(one_trip)
        return all_trips

    @classmethod
    def save(cls, trip_data, cover_photo, user_id):
        # John.jpg
        ("john", ".jpg")
        file_ext = os.path.splitext(cover_photo.filename)[1]
        # whgeywhgefwgheqwheqweqwe
        random_string = uuid.uuid4().hex
        unique_filename = random_string + file_ext
        cover_photo.save(os.path.join(app.config["UPLOAD_DIR"], unique_filename))
        data = {
            "country": trip_data["country"],
            "city": trip_data["city"],
            "length_of_stay": trip_data["length_of_stay"],
            "cover_photo": unique_filename,
            "itinerary_description": trip_data["itinerary_description"],
            "users_id": user_id
        }
        query = """
                INSERT INTO trips (country, city, length_of_stay, cover_photo, itinerary_description, users_id) 
                VALUES (%(country)s, %(city)s, %(length_of_stay)s, %(cover_photo)s, %(itinerary_description)s, %(users_id)s);
                """
        return connectToMySQL(cls.DB).query_db(query, data)

    @staticmethod
    def validate_trip(data, cover_photo):
        is_valid = True 
        if len(data['city']) < 2 or len(data['country']) < 2 or len(data['itinerary_description']) < 2:
            flash("City, Country, and/or Itinerary Description must be at least 2 characters.", "create_trip")
            is_valid = False 
        if data['length_of_stay'] == "" or int(data['length_of_stay']) < 1:
            flash("Length of stay must be at least 1 day.", "create_trip")
            is_valid = False
        if not cover_photo:
            flash("Itinerary must have a cover photo.", "create_trip")
            is_valid = False
        return is_valid

    @classmethod 
    def get_saved_by(cls, trip_id):
        data = {"trips_id": trip_id}
        query = "SELECT * FROM saved_trips WHERE trips_id=%(trips_id)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        saved = 0
        if results:
            for row in results:
                saved += 1
        return saved

    @classmethod
    def edit(cls, trip_id, cover_photo, trip_data):
        file_ext = os.path.splitext(cover_photo.filename)[1]
        random_string = uuid.uuid4().hex
        unique_filename = random_string + file_ext
        cover_photo.save( os.path.join(app.config["UPLOAD_DIR"], unique_filename))
        data = {
            "id": trip_id,
            "country": trip_data["country"],
            "city": trip_data["city"],
            "length_of_stay": trip_data["length_of_stay"],
            "cover_photo": unique_filename,
            "itinerary_description": trip_data["itinerary_description"]
        }
        query = """
                UPDATE trips
                SET country=%(country)s, city=%(city)s, length_of_stay=%(length_of_stay)s, cover_photo=%(cover_photo)s, itinerary_description=%(itinerary_description)s
                WHERE id=%(id)s;
                """
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod 
    def save_coordinates(cls, map_data, trip_id):
        data = {
            "latitude": map_data["latitude"],
            "longitude": map_data["longitude"],
            "trips_id": trip_id
        }
        query = """
                INSERT INTO map_coordinates (latitude, longitude, trips_id) 
                VALUES (%(latitude)s, %(longitude)s, %(trips_id)s);
                """
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def get_coordinates(cls, trip_id):
        data = {"id": trip_id}
        query = "SELECT * FROM map_coordinates WHERE trips_id=%(id)s;"
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def delete(cls, trip_id):
        one_trip = Trip.get_one(trip_id)
        try: 
            os.remove(os.path.join(app.config["UPLOAD_DIR"], f"{one_trip.cover_photo}"))
        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print("An error occurred.")
        data = {"id": trip_id}
        query = "DELETE FROM map_coordinates WHERE trips_id=%(id)s;"
        connectToMySQL(cls.DB).query_db(query, data)
        query = "DELETE FROM days WHERE trips_id=%(id)s;"
        connectToMySQL(cls.DB).query_db(query, data)
        query = "DELETE FROM saved_trips WHERE trips_id=%(id)s;"
        connectToMySQL(cls.DB).query_db(query, data)
        query = "DELETE FROM trips WHERE id=%(id)s;"
        return connectToMySQL(cls.DB).query_db(query, data)