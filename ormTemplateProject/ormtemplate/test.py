"""Simple Test file"""
# Django specific settings
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
# Ensure settings are read
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
# Your application specific imports
from standalone.models import Test

def clean_data():
    """Delete all data"""
    Test.objects.all().delete()


def test_setup():
    """ Test Django Model setup """
    try:
        clean_data()
        test = Test(name="name")
        test.save()
        # Check test table is not empty
        assert Test.objects.count() > 0
        print("Django Model setup completed.")
    except AssertionError as exception:
        print("Django Model setup failed with error: ")
        raise exception
    except:
        print("Unexpected error")


test_setup()
