from django.db import models
from django_autoslug.fields import AutoSlugField
from datetime import datetime

class Categorias(models.Model):
    categoria_id = models.AutoField(primary_key=True)
    categoria = models.CharField(max_length=120, null=False)


    def __unicode__(self):
        return self.categoria

    class Meta:
        verbose_name = "Categorias"
        verbose_name_plural = verbose_name


class Posts(models.Model):
    Post_id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=150, null=False)
    slug = AutoSlugField(populate_from=('titulo',), unique=True, max_length=255, overwrite=True)
    categoria = models.ForeignKey('Categorias', null=False)
    contenido = models.TextField(null=False)
    agregado = models.DateTimeField(auto_now_add=True)
    editado  = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.titulo

    class Meta:
        verbose_name = "Entradas"
        verbose_name_plural = verbose_name
    
    @models.permalink
    def get_absolute_url(self):
        return ('view_post_detail', None, { 'slug':self.slug })
