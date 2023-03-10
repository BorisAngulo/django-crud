from django.db import models



# Create your models here. 
class Post(models.Model):#heredamos para crear un modela de db
    image = models.ImageField(verbose_name='Imagen', upload_to='blog') #con verbose_name es como se mostrara en el editor y con upload_to hacemos que las imganens se guarden el img y carptea blog
    title = models.CharField(max_length=200, verbose_name='Título')
    desc = models.TextField(verbose_name='Descripción')
    content = models.TextField(verbose_name='Contenido')
    
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    update =models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:#editampos la parte del menu el titulo pequeño
        verbose_name = 'Publicación'
        verbose_name_plural = 'Publicaciones'
        ordering = ['-created']#la manera en la que se ordenaran

    def __str__(self):
        return self.title