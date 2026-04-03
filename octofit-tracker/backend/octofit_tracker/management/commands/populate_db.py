
from django.core.management.base import BaseCommand
from octofit_tracker.models import Team, User, Activity, Workout, Leaderboard
from django.utils import timezone
from django.conf import settings
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'


    def handle(self, *args, **kwargs):
        # Drop collections directly using PyMongo
        client = MongoClient(settings.DATABASES['default']['CLIENT']['host'])
        db = client[settings.DATABASES['default']['NAME']]
        db.activity.drop()
        db.leaderboard.drop()
        db.workout.drop()
        db.user.drop()
        db.team.drop()

        # Create Teams
        marvel = Team.objects.create(id=1, name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(id=2, name='DC', description='DC superheroes')

        # Create Users
        users = [
            User(id=1, name='Iron Man', email='ironman@marvel.com', team=marvel, is_leader=True),
            User(id=2, name='Captain America', email='cap@marvel.com', team=marvel),
            User(id=3, name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User(id=4, name='Batman', email='batman@dc.com', team=dc, is_leader=True),
            User(id=5, name='Superman', email='superman@dc.com', team=dc),
            User(id=6, name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
        ]
        for user in users:
            user.save()

        # Create Activities
        Activity.objects.create(id=1, user=users[0], activity_type='Running', duration_minutes=30, date=timezone.now())
        Activity.objects.create(id=2, user=users[1], activity_type='Cycling', duration_minutes=45, date=timezone.now())
        Activity.objects.create(id=3, user=users[3], activity_type='Swimming', duration_minutes=60, date=timezone.now())

        # Create Workouts
        w1 = Workout.objects.create(id=1, name='Full Body Blast', description='A full body workout')
        w2 = Workout.objects.create(id=2, name='Cardio Burn', description='High intensity cardio')
        w1.suggested_for.set([users[0], users[3]])
        w2.suggested_for.set([users[1], users[4]])

        # Create Leaderboards
        Leaderboard.objects.create(id=1, team=marvel, total_points=150)
        Leaderboard.objects.create(id=2, team=dc, total_points=120)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
