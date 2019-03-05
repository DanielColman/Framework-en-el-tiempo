"""PLatzigram views."""

# Django
from django.http import HttpResponse

# Utilities
from datetime import datetime
# Utilities
from datetime import datetime
import json

# Django
from django.http import HttpResponse


def hello_world(request):
    """Return a greeting"""
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Oh, hi: Current server time is {now}'.format(now=str(now)))

def sort_int(request):
    """Return Json response Sorted."""
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'Ingegers sorted susccessfully.'
    }
    #import pdb; pdb.set_trace()
    return HttpResponse(
        json.dumps(data, indent=4),
        content_type='application/json'
)


def say_hi(request, name, age):
    if age<12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hello {}! Welcome to Platzigram'.format(name)
    return HttpResponse(message)
