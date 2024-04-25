from django.db import models

class Article(models.Model):
    title=models.CharField('Title', max_length=200)
    text=models.TextField()