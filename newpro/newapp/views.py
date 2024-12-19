from django.shortcuts import render,redirect
from.models import*

# Create your views here.
def index(request):
    if request.POST:
        title=request.POST.get("data")
        obj=Todoitem(title=todo123)
        print(title)
        return redirect("index")
    data=Todoitem.objects.all
    return render(request,"index.html")

