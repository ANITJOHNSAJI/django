from django.shortcuts import render,redirect
from.models import*

# Create your views here.
def index(request):
    if request.POST:
        todo1=request.POST.get("data")
        todo2=request.POST.get("date")
        obj=Todoitem(tite1=todo1,title2=todo2)
        obj.save()
        return redirect("index")
    data=Todoitem.objects.all
    return render(request,"index.html",{"data":data})

