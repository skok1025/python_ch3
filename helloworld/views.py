from django.db.models import Max, F
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from helloworld.models import Counter


def hello(request):
    return render(request, 'helloworld/hello.html')


def hello3(request):
    jsonresult = {
        'result':'success',
        'data':['hello', 1, 2, True,('a', 'b', 'c')]
    }

    return JsonResponse(jsonresult)


def counter_add(request):
    c = Counter()
    c.groupno = 1
    c.depth = 1
    c.orderno = 1
    c.save()

    c = Counter()
    c.groupno = 1
    c.depth = 1
    c.orderno = 2
    c.save()

    c = Counter()
    c.groupno = 1
    c.depth = 1
    c.orderno = 3
    c.save()
    return HttpResponse('ok')


def counter_update(request):
    # orderno 1씩 증가
    # __gt, __lt, __gte ...
    Counter.objects.filter(groupno=1).filter(orderno__gte= 2).update(orderno=F('orderno')+1)
    # F() : 현재 테이블의 컬럼에 +1

    return HttpResponse('ok')


def counter_max(request):
    value = Counter.objects.aggregate(max_groupno = Max('groupno'))
    max_groupno  = 0 if value["max_groupno"] is None else value["max_groupno"]
    return HttpResponse(f'max groupno:{max_groupno}')

