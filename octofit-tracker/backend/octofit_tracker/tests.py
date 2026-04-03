from django.test import TestCase
from .models import Team, User, Activity, Workout, Leaderboard

class BasicModelTest(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(id=1, name="Test Team")
        self.assertEqual(str(team), "Test Team")

    def test_user_creation(self):
        team = Team.objects.create(id=2, name="Team2")
        user = User.objects.create(id=1, name="Test User", email="test@example.com", team=team)
        self.assertEqual(str(user), "Test User")

    def test_activity_creation(self):
        team = Team.objects.create(id=3, name="Team3")
        user = User.objects.create(id=2, name="User2", email="user2@example.com", team=team)
        activity = Activity.objects.create(id=1, user=user, activity_type="Run", duration_minutes=30, date="2024-01-01")
        self.assertIn("Run", str(activity))

    def test_workout_creation(self):
        workout = Workout.objects.create(id=1, name="Pushups")
        self.assertEqual(str(workout), "Pushups")

    def test_leaderboard_creation(self):
        team = Team.objects.create(id=4, name="Team4")
        leaderboard = Leaderboard.objects.create(id=1, team=team, total_points=100)
        self.assertIn("Team4", str(leaderboard))