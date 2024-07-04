from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class Editor(models.Model):
    nome_editor = models.CharField(max_length=200)

    def __str__(self):
        return self.nome_editor


class Noticia(models.Model):
    editor = models.ForeignKey(Editor, on_delete=models.CASCADE)
    titulo_noticia = models.CharField(max_length=200, null=False)
    texto_noticia = models.TextField(null=True)
    data_noticia = models.DateTimeField()
    imagem = models.ImageField(upload_to='media')

    def __str__(self):
        return self.titulo_noticia


class Comentario(models.Model):
    nome_utilizador = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo_noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE, null=True)
    texto_comentario = models.TextField(null=True)
    data_comentario = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.nome_utilizador}, {self.titulo_noticia}'
