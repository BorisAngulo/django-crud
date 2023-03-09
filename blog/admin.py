from django.contrib import admin

#models
from .models import Post

# Register your models here.
#admin.site.register(Post)#Agregamos al panel del administrador nuestra base de datos

@admin.register(Post)#Agregamos al panel del administrador nuestra base de datos
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'title', 'desc', 'created')#Editamos las tuplas o inormacion en panel admin
    list_display_links=('id','title',)#cambiamos el link a cualquier de las tuplas
    list_filter=('created', 'update')#añade un filtro
    search_fields=('title', 'desc')#añadimos un buscador

    readonly_fields=('created', 'update')#añade datos en solo lectura
