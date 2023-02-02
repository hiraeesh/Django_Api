from django.shortcuts import render

# Create your views here.

def mydb(request):
    dict=['value','value2']
    return render(request,'index.html',{'dict':dict})  


def myabcb(request):
    dict=['value','value2']
    return render(request,'index.html',{'dict':dict})  