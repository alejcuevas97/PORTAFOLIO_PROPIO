from django.contrib import admin
from django.urls import path,include
from .views import HomeViews,AboutView,PerfilView,ResumeView,ContactView,ProyectoView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', HomeViews.as_view(), name = "home"),
    path('about/', AboutView.as_view(), name = "about"),
    path('perfil/', PerfilView.as_view(), name = "perfil"),
    path('resume/', ResumeView.as_view(), name = "resume"),
    path('contact/', ContactView.as_view(), name = "contact"),
    path("__reload__/", include("django_browser_reload.urls")),
    
    

    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
    urlpatterns += [
        path("__reload__/", include("django_browser_reload.urls"))
    ]
    