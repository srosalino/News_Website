from django.contrib import admin

from .models import Editor, Noticia, Comentario

# Register your models here.

admin.site.register(Editor)
admin.site.register(Noticia)
admin.site.register(Comentario)
