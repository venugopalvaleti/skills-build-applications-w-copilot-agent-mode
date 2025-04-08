from django.core.management.base import BaseCommand
from pymongo import MongoClient
from django.conf import settings
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient(settings.DATABASES['default']['HOST'], settings.DATABASES['default']['PORT'])
        db = client[settings.DATABASES['default']['NAME']]

        # Clear existing collections
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activity.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # Insert users
        users = [
            {"_id": ObjectId(), "username": "user1", "email": "user1@example.com", "password": "password1"},
            {"_id": ObjectId(), "username": "user2", "email": "user2@example.com", "password": "password2"},
            {"_id": ObjectId(), "username": "user3", "email": "user3@example.com", "password": "password3"},
        ]
        db.users.insert_many(users)

        # Insert team
        team = {"_id": ObjectId(), "name": "Team A", "members": [user["_id"] for user in users]}
        db.teams.insert_one(team)

        # Insert activities
        activities = [
            {"_id": ObjectId(), "user": users[0]["_id"], "activity_type": "Running", "duration": 30},
            {"_id": ObjectId(), "user": users[1]["_id"], "activity_type": "Cycling", "duration": 45},
            {"_id": ObjectId(), "user": users[2]["_id"], "activity_type": "Swimming", "duration": 60},
        ]
        db.activity.insert_many(activities)

        # Insert leaderboard entries
        leaderboard_entries = [
            {"_id": ObjectId(), "user": users[0]["_id"], "score": 100},
            {"_id": ObjectId(), "user": users[1]["_id"], "score": 90},
            {"_id": ObjectId(), "user": users[2]["_id"], "score": 80},
        ]
        db.leaderboard.insert_many(leaderboard_entries)

        # Insert workouts
        workouts = [
            {"_id": ObjectId(), "name": "Workout 1", "description": "Description for Workout 1"},
            {"_id": ObjectId(), "name": "Workout 2", "description": "Description for Workout 2"},
            {"_id": ObjectId(), "name": "Workout 3", "description": "Description for Workout 3"},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data using pymongo.'))
