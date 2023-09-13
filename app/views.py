from django.shortcuts import render
from app.models import *
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def inserttopic(request):
    ETFO=TopicForm()
    d={'ETFO':ETFO}
    if request.method=='POST':
        DTFO=TopicForm(request.POST)
        if DTFO.is_valid():
            DTFO.save()
            return HttpResponse('Topic data is created')

    return render(request,'insert_topic.html',d)

def insertwebpage(request):
    EWFO=WebpageForm()
    d1={'EWFO':EWFO}
    if request.method=='POST':
        DWFO=WebpageForm(request.POST)
        if DWFO.is_valid():
            DWFO.save()
            return HttpResponse('Webpage data is created')
    return render(request,'insert_webpage.html',d1)