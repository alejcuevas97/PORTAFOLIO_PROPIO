from django.views.generic import View
from django.shortcuts import render
from .serializers import portafolioSerializers
from rest_framework import viewsets
from porfolio.models import Project


class portafolioViewset(viewsets.ModelViewSet):
    queryset= Project.objects.all()
    serializer_class= portafolioSerializers


class HomeViews(View):
    def get(self,request, *args, **kwargs):
        context={
            
        }
        return render(request, 'index.html', context)
    
class PerfilView(View):
    def get(self, request, *args, **kwargs):
        
        context={
            
        }
        return render(request, 'perfil.html', context)    
    
class AboutView(View):
    def get(self, request, *args, **kwargs):
        
        context={
            
        }
        return render(request, 'about.html', context)    
    
class ResumeView(View):
    def get(self, request, *args, **kwargs):
        
        context={
            
        }
        return render(request, 'resume.html', context)     
    
    

class ContactView(View):
    def get(self, request, *args, **kwargs):
        
        context={
            
        }
        return render(request, 'contact.html', context)      
    
class ProyectoView(View):
    def get (self, request, *args, **kwargs):
        
        context={
            
        }
        return render(request, 'proyectos.html', context)
    
   