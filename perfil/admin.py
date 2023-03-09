from django.contrib import admin

#Models
from .models import Project
# Register your models here

@admin.register(Project)#Agregamos al panel del administrador nuestra base de datos
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'desc', 'created')#Editamos las tuplas o inormacion en panel admin
    #list_editable = ('title')#Con esto hacemos el titulo editable desde la lista
    list_display_links=('id','title',)#cambiamos el link a cualquier de las tuplas
    list_filter=('created', 'update')#añade un filtro
    search_fields=('title', 'desc')#añadimos un buscador

    readonly_fields=('created', 'update')#añade datos en solo lectura


