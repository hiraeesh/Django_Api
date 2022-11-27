from django.shortcuts import render
from data.forms import Userdata
from django.http import HttpResponse

# Create your views here.
def index(request):
    if request.method=='POST':
        fm=Userdata(request,'POST')
        if fm.is_valid():
            fm.save()
            return HttpResponse("data save")
    else:
        fm=Userdata()
        return render(request,'index.html',{'fm':fm})


    