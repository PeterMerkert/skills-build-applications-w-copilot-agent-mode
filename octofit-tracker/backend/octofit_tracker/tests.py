from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile, Team, Activity, Leaderboard, Workout
from datetime import timedelta, date, time

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(username='testuser', password='testpass')
        self.assertEqual(user.username, 'testuser')

class ProfileModelTest(TestCase):
    def test_create_profile(self):
        user = User.objects.create_user(username='testuser2', password='testpass')
        profile = Profile.objects.create(user=user, bio='Test bio')
        self.assertEqual(profile.user.username, 'testuser2')

class TeamModelTest(TestCase):
    def test_create_team(self):
        user = User.objects.create_user(username='testuser3', password='testpass')
        team = Team.objects.create(name='Test Team')
        team.members.add(user)
        self.assertIn(user, team.members.all())

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create_user(username='testuser4', password='testpass')
        activity = Activity.objects.create(
            user=user,
            activity_type='running',
            duration=timedelta(minutes=30),
            distance=5.0,
            calories_burned=300,
            date=date.today(),
            time=time(8, 0),
        )
        self.assertEqual(activity.user.username, 'testuser4')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        user = User.objects.create_user(username='testuser5', password='testpass')
        leaderboard = Leaderboard.objects.create(user=user, score=100)
        self.assertEqual(leaderboard.score, 100)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        user = User.objects.create_user(username='testuser6', password='testpass')
        workout = Workout.objects.create(
            name='Test Workout',
            description='Test workout description',
            duration=timedelta(minutes=45),
            difficulty_level=2,
            activity_type='cycling',
            created_by=user,
        )
        self.assertEqual(workout.name, 'Test Workout')
