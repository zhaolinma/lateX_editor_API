from django.db import models

# Create your models here.

class Article(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now=True)
    detail = models.TextField()
    title = models.CharField(max_length=100)
