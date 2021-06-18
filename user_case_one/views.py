from django.shortcuts import render
from .models import usage_log, log_entry
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .forms import UsageForm, LogForm


# Create your views here.
def login(request):
    print("Entered view function")
    db_store = usage_log(
        User='ravi',
        Month='Nov. 4, 2020',
        Source='Mobile',
        Total_calls=2,
        First_api_call='Nov. 4, 2020, 1:45 p.m',
        Last_api_call='Nov. 7, 2020, 1:45 p.m',
        Last_checked_row=12
    )
    db_store.save()
    print("finished save")
    # return {"store": "success"}
    return HttpResponse(status=201)


def store_log_entry(request):
    print("Entered view function for store log")
    db_store = log_entry(
        Api_url='/get/store_log',
        Method='GET',
        User_email='ravi@gmail.com',
        Milliseconds=300,
        Code=200,
        User_agent='Chrome/89.0',
        Time='June 10, 2020, 1:45 p.m'
    )
    db_store.save()
    print("finished save")
    return HttpResponse(status=201)


@csrf_exempt
def change_log_entry(request):
    '''if request.method == "GET":
        print("getting_data")
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        content = body["id"]
        print(content)'''
    print("getting_data")
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    content = body["id"]
    print(content)
    get_data = log_entry.objects.filter(id=content).values()
    # get_data = log_entry.objects.get(id=content)
    print(get_data)
    for i in get_data:
        print(i)
    return HttpResponse(status=201)


@csrf_exempt
def change_log_entry(request, pk):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    print(body)
    print("getting_data")
    print(pk)
    #re = request.POST
    re = request.body
    print(re)
    obj = get_object_or_404(log_entry, id=pk)
    print(obj)
    form = LogForm(body or None, instance=obj)
    print(form)
    #form.save()
    if form.is_valid():
        print("saving")
        form.save()
    return HttpResponse(status=201)


def change_usage_log(request):
    pass
