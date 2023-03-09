from django.db import models

# Create your models here.
class Project(models.Model):
    title=models.CharField(max_length=200, verbose_name='Título')
    desc=models.TextField(verbose_name='Descripción')

    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    update =models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')

    class Meta:#editampos la parte del menu el titulo pequeño
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ['-created']#la manera en la que se ordenaran

    def __str__(self):
        return self.title