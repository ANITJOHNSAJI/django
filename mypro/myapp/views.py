from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def index(request):
    if request.POST:
        title=request.POST.get("data")
        obj=Todoitem(title1=title)
        obj.save()
        return redirect("index")
    obj=Todoitem.objects.all()
    return render(request,"index.html",{"files":obj})

def about(request):
    return render(request,"about.html")