# Generated by Django 2.2.4 on 2019-09-04 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_todo_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='priority',
            field=models.TextField(choices=[('urgent', 'urgent'), ('average', 'average'), ('flexible', 'flexible')], default='average'),
        ),
    ]
