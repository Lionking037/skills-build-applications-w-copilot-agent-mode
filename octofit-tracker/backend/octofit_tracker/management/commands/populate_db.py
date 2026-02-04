from django.core.management.base import BaseCommand
from django.conf import settings
from django.db import connections

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        db = connections['default'].cursor().db_conn
        # Drop collections if they exist
        for col in ['users', 'teams', 'activities', 'leaderboard', 'workouts']:
            if col in db.list_collection_names():
                db[col].drop()

        # Create unique index on email for users
        db['users'].create_index('email', unique=True)

        # Insert test users
        users = [
            {'name': 'Iron Man', 'email': 'ironman@marvel.com', 'team': 'marvel'},
            {'name': 'Captain America', 'email': 'cap@marvel.com', 'team': 'marvel'},
            {'name': 'Batman', 'email': 'batman@dc.com', 'team': 'dc'},
            {'name': 'Wonder Woman', 'email': 'wonderwoman@dc.com', 'team': 'dc'},
        ]
        db['users'].insert_many(users)

        # Insert test teams
        teams = [
            {'name': 'marvel', 'members': ['ironman@marvel.com', 'cap@marvel.com']},
            {'name': 'dc', 'members': ['batman@dc.com', 'wonderwoman@dc.com']},
        ]
        db['teams'].insert_many(teams)

        # Insert test activities
        activities = [
            {'user_email': 'ironman@marvel.com', 'activity': 'run', 'distance': 5},
            {'user_email': 'cap@marvel.com', 'activity': 'cycle', 'distance': 10},
            {'user_email': 'batman@dc.com', 'activity': 'swim', 'distance': 2},
            {'user_email': 'wonderwoman@dc.com', 'activity': 'run', 'distance': 8},
        ]
        db['activities'].insert_many(activities)

        # Insert test leaderboard
        leaderboard = [
            {'team': 'marvel', 'points': 15},
            {'team': 'dc', 'points': 10},
        ]
        db['leaderboard'].insert_many(leaderboard)

        # Insert test workouts
        workouts = [
            {'user_email': 'ironman@marvel.com', 'workout': 'pushups', 'reps': 50},
            {'user_email': 'batman@dc.com', 'workout': 'situps', 'reps': 40},
        ]
        db['workouts'].insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
