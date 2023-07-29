# Generated by Django 4.2.2 on 2023-07-29 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topics',
            name='summary',
            field=models.TextField(blank=True, max_length=300, null=True, verbose_name='Название темы'),
        ),
        migrations.AlterField(
            model_name='topics',
            name='discriptions',
            field=models.TextField(blank=True, max_length=300, null=True, verbose_name='Описание темы'),
        ),
    ]
