# Generated by Django 2.2.4 on 2019-09-02 13:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_todo'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='due_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
    ]