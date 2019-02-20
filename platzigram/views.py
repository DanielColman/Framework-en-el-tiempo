"""PLatzigram views."""

#Django
from django.http import HttpResponse

#Utilities
from datetime import datetime
# Utilities
from datetime import datetime

# Django
from django.http import HttpResponse


def hello_world(request):
    """Return a greeting"""
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Oh, hi: Current server time is {now}'.
            format(now=str(now))
    )

def hi(request):
    """Hi."""
    import pdb
    pdb.set_trace()
    return HttpResponse('Hi!')