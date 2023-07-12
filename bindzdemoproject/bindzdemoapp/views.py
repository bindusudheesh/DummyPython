from django.http import HttpResponse
from django.shortcuts import render

from bindzdemoapp.models import Place, Team


# Create your views here.
def demo(request):
    obj = Place . objects.all()
    objct = Team.objects.all()
    return render (request,"index.html",{'result':obj,'out':objct})

# def register(request):
#     return render(request,"register.html")


# def demo(request):
#     return render(request,"index.html")
