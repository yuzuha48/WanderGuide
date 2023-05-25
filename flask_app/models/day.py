from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import trip 
from flask import flash
import base64

class Day:
    DB = "trips_schema"
    def __init__(self, data):
        self.id = data["id"]
        self.day_theme = data["day_theme"]
        self.location = data["location"]
        self.activity = data["activity"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.trip = None
        self.map_coordinates = []

    @classmethod
    def get_all(cls):
        query = """ SELECT * FROM days 
                JOIN trips ON trips.id = trips.days_id
                """
        results = connectToMySQL(cls.DB).query_db(query)
        all_days = []
        if results:
            for row in results:
                one_day = cls(row)
                trip_data = {
                    "id": row['trips.id'], 
                    "country": row["country"],
                    "city": row["city"],
                    "length_of_stay": row["length_of_stay"],
                    "cover_photo": row["cover_photo"],
                    "itinerary_description": row["itinerary_description"],
                    # "interests": row["interests"],
                    "created_at": row['trips.created_at'],
                    "updated_at": row['trips.updated_at']
                }
                one_day.trip = trip.Trip(trip_data)
                all_days.append(one_day)
        return all_days

    @classmethod
    def save(cls, day_data, trip_id):
        data = {
            "day_theme": day_data["day_theme"],
            "location": day_data["location"],
            "activity": day_data["activity"],
            "trips_id": trip_id
        }
        query = """
                INSERT INTO days (day_theme, location, activity, trips_id) 
                VALUES (%(day_theme)s, %(location)s, %(activity)s, %(trips_id)s);
                """
        return connectToMySQL(cls.DB).query_db(query, data)

    @staticmethod
    def validate_day(data):
        errors = {}
        if len(data['day_theme']) < 2:
            errors['day_theme'] = "Description of Day must be at least 2 characters."
        if len(data['location']) < 2:
            errors['location'] = "Location must be at least 2 characters."
        if len(data['activity']) < 2:
            errors['activity'] = "Activity must be at least 2 characters."
        return errors

    @classmethod
    def edit(cls, day_id, day_data):
        data = {
            "id": day_id,
            "day_theme": day_data["day_theme"],
            "location": day_data["location"],
            "activity": day_data["activity"]
        }
        query = """
                UPDATE days
                SET day_theme=%(day_theme)s, location=%(location)s, activity=%(activity)s
                WHERE id=%(id)s;
                """
        return connectToMySQL(cls.DB).query_db(query, data)