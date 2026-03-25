from django.shortcuts import render
from .models import Project

def Proyectos(request):
    proyectos= Project.objects.all()
    return render (request, 'portafolio/proyectos.html',{'proyectos':proyectos})
