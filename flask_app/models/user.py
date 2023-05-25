from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import trip
from flask import flash
from flask_app import app
import re
from flask_bcrypt import Bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
bcrypt = Bcrypt(app)

class User:
    DB = "trips_schema"
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.trips = []
        self.saved_trips = []

    @classmethod
    def save(cls, user_data):
        pw_hash = bcrypt.generate_password_hash(user_data['password'])
        data = {
            "first_name": user_data["first_name"], 
            "last_name": user_data["last_name"],
            "email": user_data["email"], 
            "password": pw_hash
        }
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL(cls.DB).query_db(query, data)

    @staticmethod
    def validate_user(data):
        is_valid = True
        if len(data["first_name"]) < 2 or len(data["last_name"]) < 2:
            flash("First name and/or last name must be at least 2 characters.", "registration")
            is_valid = False
        if data["first_name"].isalpha() == False or data["last_name"].isalpha() == False:
            flash("First name and/or last name may only contain letters.", "registration")
            is_valid = False
        if not EMAIL_REGEX.match(data["email"]):
            flash("Email address is invalid.", "registration")
            is_valid = False
        if User.get_by_email(data):
            flash("Email is associated with an existing user.", "registration")
            is_valid = False
        if len(data["password"]) < 8:
            flash("Password must be at least 8 characters.", "registration")
            is_valid = False
        if data["confirm_password"] != data["password"]:
            flash("Passwords do not match.", "registration")
            is_valid = False
        return is_valid

    @classmethod
    def get_one(cls, user_id):
        data = {"id": user_id}
        query = "SELECT * FROM users WHERE id=%(id)s;"
        result = connectToMySQL(cls.DB).query_db(query, data)
        if result:
            user = cls(result[0])
            return user

    @classmethod
    def get_all(cls):
        query = "SELECT * from users;"
        results = connectToMySQL(cls.DB).query_db(query)
        all_users = []
        if results:
            for one_user in results:
                all_users.append(cls(one_user))
        return all_users

    @classmethod 
    def get_by_email(cls, user_data):
        data = {"email": user_data["email"]}
        query = "SELECT * FROM users WHERE email=%(email)s;"
        result = connectToMySQL(cls.DB).query_db(query, data)
        if len(result) < 1:
            return False 
        return cls(result[0]) 

    @classmethod 
    def get_my_trips(cls, user_id):
        data = {"id": user_id}
        query = """
                SELECT * FROM users
                LEFT JOIN trips ON users.id = trips.users_id
                WHERE users.id=%(id)s;
                """
        result = connectToMySQL(cls.DB).query_db(query, data)
        user = cls(result[0])
        for row in result:
            if row["trips.id"]:
                user.trips.append(trip.Trip.get_one(row["trips.id"]))
        return user
    
    @classmethod
    def save_trip(cls, user_id, trip_id):
        data = {
            "users_id": user_id, 
            "trips_id": trip_id
        }
        query = "INSERT INTO saved_trips (users_id, trips_id) VALUES (%(users_id)s, %(trips_id)s);"
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def get_saved_trips(cls, user_id):
        data = {"users_id": user_id}
        query = "SELECT * FROM saved_trips WHERE users_id=%(users_id)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        one_user = User.get_one(user_id)        
        if results:
            for row in results:
                one_user.saved_trips.append(trip.Trip.get_one(row["trips_id"]))
        return one_user

    @classmethod
    def unsave_trip(cls, user_id, trip_id):
        data = {
            "users_id": user_id, 
            "trips_id": trip_id
        }
        query = "DELETE FROM saved_trips WHERE users_id=%(users_id)s AND trips_id=%(trips_id)s;"
        return connectToMySQL(cls.DB).query_db(query, data)



