# Generated by Django 2.2.4 on 2019-09-02 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_todo_due_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='status',
            field=models.TextField(choices=[('on process', 'on process'), ('done', 'done')], default='on process'),
        ),
    ]
