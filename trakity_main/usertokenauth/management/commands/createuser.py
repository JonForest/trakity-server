from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    help = 'Create a user. Usage `python manage.py createuser <username> <password>`'

    def add_arguments(self, parser):
        # Positional arguments that require no switches
        parser.add_argument('email')
        parser.add_argument('password')

    def handle(self, *args, **options):
        user = User.objects.create_user(username='not_set', email=options['email'], password=options['password'])
        user.save()
        print('User created')
