from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(username='testuser', email='test@example.com', first_name='Test', last_name='User')
        self.assertEqual(user.username, 'testuser')

class TeamModelTest(TestCase):
    def test_create_team(self):
        user = User.objects.create(username='testuser2', email='test2@example.com', first_name='Test', last_name='User')
        team = Team.objects.create(name='Test Team')
        team.members.add(user)
        self.assertEqual(team.name, 'Test Team')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create(username='testuser3', email='test3@example.com', first_name='Test', last_name='User')
        activity = Activity.objects.create(user=user, activity_type='Running', duration=30, calories_burned=300, date='2024-01-01')
        self.assertEqual(activity.activity_type, 'Running')

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        user = User.objects.create(username='testuser4', email='test4@example.com', first_name='Test', last_name='User')
        workout = Workout.objects.create(user=user, name='Morning Run', description='A quick run', date='2024-01-02')
        self.assertEqual(workout.name, 'Morning Run')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        user = User.objects.create(username='testuser5', email='test5@example.com', first_name='Test', last_name='User')
        leaderboard = Leaderboard.objects.create(user=user, score=100, rank=1)
        self.assertEqual(leaderboard.rank, 1)
