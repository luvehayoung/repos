from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=32)
    email = models.EmailField()

class Todo(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
