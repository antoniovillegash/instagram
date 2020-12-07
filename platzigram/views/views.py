"""platzigram views"""
"""django"""
from django.http import HttpResponse
"""utilities"""
from datetime import datetime
import json


"""escribimos una vista, estas siempre reciben un request"""
def hello_world(request):
    """Return a hello world"""
    now = datetime.now().strftime('%b/%dth, %Y - %H:%M hrs')
    return HttpResponse('hello world! la hora es: {now}'.format(
        now=str(now)
        ))

def sort_integers(request):
    """sort_integers"""
    # debug
    # import pdb
    # pdb.set_trace()
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    data = {
        'status':'ok',
        'numbers':sorted_ints,
        'message':'numeros sorteados'
    }


    # import pdb
    # pdb.set_trace()
    return HttpResponse(
        json.dumps(data), 
        content_type='application/json'
        )

def say_hi(request, name, age):
    """say_hi"""
    if age < 12:
        message = 'sorry {} you are not allowed to be here'.format(name)
    else:
        message = 'Hello {}! Welcome to platzigram'.format(name)

    data = {
        'status':'ok',
        'message':message
    }

    return HttpResponse(
        json.dumps(data), 
        content_type='application/json'
        )