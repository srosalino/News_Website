# Generated by Django 4.0.4 on 2022-05-09 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Editor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_editor', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Utilizador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_utilizador', models.CharField(max_length=200)),
                ('email_utilizador', models.EmailField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_noticia', models.CharField(max_length=200)),
                ('texto_noticia', models.TextField(null=True)),
                ('data_noticia', models.DateTimeField()),
                ('imagem', models.ImageField(upload_to='C:/Cursos_Profissionais/Programação Avançada com Python/Django_SR/Imagens_noticias')),
                ('editor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp1.editor')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto_comentario', models.TextField(null=True)),
                ('nome_utilizador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp1.utilizador')),
            ],
        ),
    ]
