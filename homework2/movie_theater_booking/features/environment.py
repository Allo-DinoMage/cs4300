import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie_theater_booking.settings')
django.setup()

def before_all(context):
    """
    Set up Django test environment once before all tests.
    """
    from django.test.utils import setup_test_environment
    setup_test_environment()

def before_scenario(context, scenario):
    """
    Flush the database before each scenario for a clean state.
    """
    from django.core.management import call_command
    call_command('flush', '--no-input', verbosity=0)

def after_scenario(context, scenario):
    """
    Clean up after each scenario.
    """
    pass
