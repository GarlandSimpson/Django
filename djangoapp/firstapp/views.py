"""Contains view functions/classes"""
from datetime import date
from django.http import HttpResponse


def index(request):
    """returns HTTP response"""
    # Create a simple html page as a string
    template = "<html>This is your first view</html>"
    # return the template as content argument in HTTP response
    return HttpResponse(content=template)


def get_date(request):
    """returns today's date"""
    today = date.today()
    template = "<html>Today's date is {}</html>".format(today)
    # return the template as content argument in HTTP response
    return HttpResponse(content=template)
