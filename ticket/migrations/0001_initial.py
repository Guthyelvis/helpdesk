# Generated by Django 2.0.8 on 2018-09-24 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.CharField(max_length=14)),
                ('anexo', models.FileField(blank=True, upload_to='post_image')),
                ('descricao', models.TextField()),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ticket.Categoria')),
            ],
        ),
    ]