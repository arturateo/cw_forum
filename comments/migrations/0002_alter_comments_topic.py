# Generated by Django 4.2.2 on 2023-07-29 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0004_remove_topics_discriptions_topics_description'),
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_topic', to='topics.topics', verbose_name='Топик'),
        ),
    ]