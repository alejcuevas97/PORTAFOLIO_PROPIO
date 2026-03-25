from django.db import models

class Project(models.Model):
    title=models.CharField(max_length=150, verbose_name='Titulo')
    descriptions=models.TextField(verbose_name='Descripcion')
    image=models.ImageField(upload_to='Proyecto', verbose_name='Imagen')
    link=models.URLField(max_length=150, verbose_name='Enlace')
    created=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creacion')
    update=models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualizacion')
    
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='Proyecto'
        verbose_name_plural='Proyectos'
        ordering=['-created']
    
