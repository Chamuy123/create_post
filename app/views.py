from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.models import *

def topic(request):
    if request.method=='POST':
        tn=request.POST['tn']

        to=Topic.objects.get_or_create(tname=tn)[0]
        to.save()
        QLTO=Topic.objects.all()
        d={'topic':QLTO}

        return render(request,'display_topic.html',d)

    return render(request,'topic.html')

def webpage(request):
    QLTO=Topic.objects.all()
    d={'topic':QLTO}
    if request.method=="POST":
        tn=request.POST['tn']
        na=request.POST['na']
        ur=request.POST['ur']
        em=request.POST['em']

        to=Topic.objects.get(tname=tn)
        WO=Webpage.objects.get_or_create(tname=to,name=na,url=ur,email=em)[0]
        WO.save()
        QLWO=Webpage.objects.all()
        d1={'webpage':QLWO}        
        return render(request,'display_webpage.html',d1)
    return render(request,'webpage.html',d)

def Accessrecord(request):
    QLWO=Webpage.objects.all()
    d={'webpage':QLWO}
    if request.method=="POST":
        #pk=request.POST['pk']
        na=request.POST['na']
        au=request.POST['au']
        da=request.POST['da']

        WO=Webpage.objects.get(pk=na)
        AO=AccessRecord.objects.get_or_create(name=WO,author=au,date=da)[0]
        AO.save()
        QLAO=AccessRecord.objects.all()
        d={'record':QLAO}
        return render(request,'display_accessrecord.html',d)
    return render(request,'Accessrecord.html',d)


def select_multiple_webpage(request):
    QLTO=Topic.objects.all()
    d={'topic':QLTO}
    if request.method=='POST':
        topiclist=request.POST.getlist('tn')
        QLWO=Webpage.objects.none()
        for i in topiclist:
            QLWO=QLWO|Webpage.objects.filter(tname=i)
        d1={'webpage':QLWO}
        return render(request,'display_webpage.html',d1)

    return render(request,'select_multiple_webpage.html',d)


def select_multiple_accessrecord(request):
    QLWO=Webpage.objects.all()
    d={'webpage':QLWO}
    if request.method=='POST':
        topiclist=request.POST.getlist('na')
        QLAO=AccessRecord.objects.none()
        for i in topiclist:
            QLAO=QLAO|AccessRecord.objects.filter(name=i)
        d1={'record':QLAO}
        return render(request,'display_accessrecord.html',d1)
        
    return render(request,'select_multiple_accessrecord.html',d)

def checkbox_webpage(request):
    QLTO=Topic.objects.all()
    d={'topic':QLTO}
    return render(request,'checkbox_webpage.html',d)

def checkbox_accessrecord(request):
    QLWO=Webpage.objects.all()
    d={'webpage':QLWO}
    return render(request,'checkbox_accessrecord.html',d)


