# Generated by Django 3.2.4 on 2021-07-06 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Colaboradores',
            fields=[
                ('idColaboradores', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='RUT Colaborador')),
                ('nomColaboradores', models.CharField(max_length=30, verbose_name='Nombre Colaborador')),
                ('telefono', models.IntegerField(max_length=9, verbose_name='Telefono')),
                ('direccion', models.CharField(max_length=30, verbose_name='Dirección')),
                ('email', models.CharField(max_length=30, verbose_name='Email')),
                ('pais', models.CharField(max_length=20, verbose_name='país')),
            ],
        ),
    ]
