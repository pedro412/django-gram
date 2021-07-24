from django.http.response import HttpResponse, JsonResponse
from datetime import datetime


def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Current server time is {now}'.format(
        now=now
    ))


def sort_integers(request):
    list = request.GET.getlist('numbers')[0].split(',')
    intList = [int(i) for i in list]
    return JsonResponse({
        'status': 'ok',
        'numbers': sorted(intList, key=float)
    })


def say_hi(request, name, age):
    if age < 12:
        message = 'Sorry {} you are not allowed here'.format(name)
    else:
        message = 'Hi, {} welcome to platzigram'.format(name)

    return JsonResponse({
        'status': 'ok',
        'message': message
    })
