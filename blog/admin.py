from django.forms import ModelForm
from django.contrib import admin
from suit_redactor.widgets import RedactorWidget
from .models import Categorias, Posts


class PostForm(ModelForm):
    class Meta:
        widgets = {
            'contenido': RedactorWidget(editor_options={'lang': 'es'})
        }


class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'slug', 'categoria','agregado',)
    form = PostForm
    fieldsets = [
        (' ', {'fields': ('titulo',)}),
        (' ', {'fields': ('contenido',)}),
        (' ', {'fields': ('categoria',)}),

    ]


admin.site.register(Categorias)
admin.site.register(Posts, PostAdmin)

