from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    header = models.CharField(max_length=100, null=True)
    text = models.TextField(max_length=3900)

    def __str__(self):
        return self.title


class Link(models.Model):
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=150)

    def __str__(self):
        return self.name
