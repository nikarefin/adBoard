from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(
        max_length=32,
        unique=True
    )

    def __str__(self):
        return f'{self.name}'


class Ad(models.Model):
    title = models.CharField(
        max_length=128
    )
    content = RichTextField(
        blank=True,
        null=True
    )
    author = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        to=Category,
        on_delete=models.CASCADE
    )
    date = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('ads', args=[str(self.id)])


class Response(models.Model):
    text = models.TextField()
    date = models.DateTimeField(
        auto_now_add=True
    )
    ad = models.ForeignKey(
        to=Ad,
        on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )
    status = models.CharField(
        max_length=8,
        default='None'
    )

    def __str__(self):
        return f'{self.text}'
