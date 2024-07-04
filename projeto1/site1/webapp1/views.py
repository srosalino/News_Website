from django.shortcuts import render, redirect
import datetime
from .models import Editor, Noticia, Comentario

from .forms import FormUser1, FormUserLogin

from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    return render(request, 'webapp1/index.html')


def registoUser(r):
    msg = ''
    if r.method == 'POST':
        form = FormUser1(r.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            msg = 'Erro! Dados incorretos!'
    return render(r, 'webapp1/registo.html', {'form': FormUser1(), 'msg': msg})


def loginUser(r):
    msg = ''
    if r.method == 'POST':
        form = FormUser1(r.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            msg = 'Erro! Dados incorretos!'
    return render(r, 'webapp1/login.html', {'form': FormUserLogin(), 'msg': msg})


def noticias(r):
    noticia = Noticia.objects.order_by('-data_noticia')
    dados = {'noticias': noticia}
    return render(r, 'webapp1/noticias.html', dados)


def detalhe(r, noticia_id):
    comentarios = Comentario.objects.filter(titulo_noticia_id=noticia_id)
    noticia = Noticia.objects.get(pk=noticia_id)
    if r.method == 'POST':
        coment_atual = r.POST['comentario']
        id_autor_comentario = r.user.id
        c = Comentario.objects.create(
            nome_utilizador_id=id_autor_comentario,
            titulo_noticia_id=noticia_id,
            texto_comentario=coment_atual,
            data_comentario=datetime.datetime.now()
        )
        c.save()
    dados = {'Noticia': noticia, 'comentarios': comentarios}
    return render(r, 'webapp1/detalhe.html', dados)
