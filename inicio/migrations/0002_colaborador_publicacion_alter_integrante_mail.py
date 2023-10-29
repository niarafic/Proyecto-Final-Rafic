# Generated by Django 4.2.6 on 2023-10-29 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Colaborador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('mail', models.EmailField(max_length=254)),
                ('universidad', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=250)),
                ('autores', models.CharField(max_length=100)),
                ('revista', models.CharField(max_length=30)),
                ('volumen', models.IntegerField()),
                ('anio', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='integrante',
            name='mail',
            field=models.EmailField(max_length=254),
        ),
    ]
