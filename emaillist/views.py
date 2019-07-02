from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
# Create your views here.
from emaillist.models import Emaillist


def add(request):
    emaillist = Emaillist()

    emaillist.first_name= request.POST['fn']
    emaillist.last_name= request.POST['ln']
    emaillist.email= request.POST['email']

    emaillist.save() # 영속화
                     # DB 와 연결되어 있는 객체

    return HttpResponseRedirect('/emaillist')


def index(request):
    emaillist = Emaillist.objects.all().order_by('-id')

    data = {
        'emaillist':emaillist
    }

    return render(request, 'emaillist/index.html',data)


def form(request):
    return render(request, 'emaillist/form.html')