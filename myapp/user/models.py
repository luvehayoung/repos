from django.db import models
import datetime

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=32)
    email = models.EmailField()

class Todo(models.Model):
    status_type = (
        ('on process', 'on process'),
        ('done', 'done'),
    )
    priority_type = (
        ('1','urgent'),
        ('2','average'),
        ('3','flexible')
    )
    title = models.CharField(max_length=100)
    content = models.TextField()
    due_date = models.DateField(("Date"), default=datetime.date.today)
    status = models.TextField(choices=status_type, default='on process')
    priority = models.TextField(choices=priority_type, default='average')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
