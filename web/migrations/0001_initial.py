# Generated by Django 3.2.5 on 2021-08-01 00:52

from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome Aluno')),
                ('nota', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Nota')),
                ('situacao', models.CharField(max_length=100, verbose_name='Situação')),

            ],
        ),
    ]
