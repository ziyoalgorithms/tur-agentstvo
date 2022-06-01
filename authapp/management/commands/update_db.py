from django.core.management.base import BaseCommand
from authapp.models import TravelUser, TravelUserProfile


class Command(BaseCommand):
    help = 'Update DB'

    def handle(self, *args, **options):
        users = TravelUser.objects.all()
        for user in users:
            user_profile = TravelUserProfile.objects.create(user=user)
            user_profile.save()
