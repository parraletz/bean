from django.contrib import admin

from .models import Categorias, Posts

class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'slug', 'categoria',)


admin.site.register(Categorias)
admin.site.register(Posts, PostAdmin)

