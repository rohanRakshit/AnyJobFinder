from django.shortcuts import render
from django.http import HttpResponse
from .models import frontInfo , detail

# Create your views here.

def fun1(request):
    data=frontInfo.objects.all()
    return render(request,"p1.html" , {'data' : data})

def fun2(request , myid):
    data = detail.objects.filter(id=myid)
    # params = {
    #     'data' : data
    # }
    return render(request,"inner.html" , {'data' : data[0]})

def fun3(request):
    return render(request , 'about.html')

def search(request):
    if(request.method == "GET"):
        text = request.GET.get('find')
        data = frontInfo.objects.filter(title__icontains=text)
        data = frontInfo.objects.filter(shortDesc__icontains=text)
        print(text)
        params = {
            'text' : data ,
            'noinfo' : text
        }
    return render(request , "search.html" , params)