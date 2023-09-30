# Generated by Django 4.2.5 on 2023-09-30 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0003_delete_sugerencia'),
    ]

    operations = [
        migrations.CreateModel(
            name='WatchList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('genero', models.CharField(max_length=100)),
                ('director', models.CharField(max_length=100)),
                ('año_lanzamiento', models.IntegerField()),
            ],
        ),
        migrations.RenameModel(
            old_name='funcion',
            new_name='ReservaPelicula',
        ),
    ]