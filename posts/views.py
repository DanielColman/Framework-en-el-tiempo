from django.shortcuts import render

#Django
from django.http import HttpResponse


#Utilities
from datetime import datetime

# Create your views here.
posts = [
    {
        'name': 'Mont Blac',
        'user': 'Daniel Colman',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=1036',
    },
    {
        'name': 'Via Láctea',
        'user': 'C. Vander',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=903',
    },
    {
        'name': 'Nuevo auditorio',
        'user': 'Thespianartist',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=1076',
    }
]


def list_posts(request):
    """"Lista de Post existentes"""
    content = []
    for post in posts:
        content.append("""
        <p><strong>{name}</strong></p>
        <p><small>{user} - <i>{timestamp}</i></p></small>
        <figure><img src="{picture}"/></img></figure>
        """.format(**post))
    return HttpResponse('<br>'.join(content))