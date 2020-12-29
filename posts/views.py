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
        'photo': 'https://www.laughtard.com/wp-content/uploads/2019/02/50-Funny-Animal-Pictures-That-You-Need-In-Your-Life-37.jpg',
        'picture': 'https://picsum.photos/200/200/?image=1036',
    },
    {
        'name': 'hola',
        'user': 'Tony Villegas',
        'timestamp': datetime.now().strftime('%b/%dth, %Y - %H:%M hrs'),
        'photo': 'https://www.laughtard.com/wp-content/uploads/2019/02/50-Funny-Animal-Pictures-That-You-Need-In-Your-Life-37.jpg',
        'picture': 'https://picsum.photos/200/200/?image=903',
    }
]


def list_posts(request):
    """listing existing posts"""

    
    return render(request, 'posts/feed.html', {'posts':posts})
