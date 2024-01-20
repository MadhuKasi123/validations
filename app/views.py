from django.shortcuts import render
from app.models import *
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):
    ETFO=TopicForm()
    d={"ETFO":ETFO}
    if request.method=='POST':
        TFDO=TopicForm(request.POST)
        TFDO.save()
        return HttpResponse('insert_topic is done')
    return render(request,'insert_topic.html',d)


def insert_webpage(request):
    EWFO=WebpageForm()
    d={'EWFO':EWFO}
    if request.method=='POST':
        WFDO=WebpageForm(request.POST)
        WFDO.save()
        return HttpResponse('insert_webpage is done')


    return render(request,'insert_webpage.html',d)

def insert_AccessRecords(request):
    EAFO=AccessRecordsForm()
    d={'EAFO':EAFO}
    if request.method=='POST':
        AFDO=AccessRecordsForm(request.POST)
        AFDO.save()
        return HttpResponse('insert_AccessRecords is done')
    return render(request,'insert_AccessRecords.html',d)