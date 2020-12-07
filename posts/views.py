"""posts views"""
# django
from django.shortcuts import render
# utilities
from datetime import datetime

posts = [
    {
        'name': 'hola',
        'user': 'Erika muñoz',
        'timestamp': datetime.now().strftime('%b/%dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=1036',
    },
    {
        'name': 'hola',
        'user': 'Tony Villegas',
        'timestamp': datetime.now().strftime('%b/%dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=903',
    }
]


def list_posts(request):
    """listing existing posts"""

    
    return render(request, 'feed.html', {'posts':posts})
