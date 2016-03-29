from __future__ import unicode_literals

from django.db import models


# Create your models here.


class BlogPost(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user_id = models.IntegerField()
    content = models.TextField()
    title = models.CharField(max_length=100, default='')
    owner = models.ForeignKey('auth.User', related_name='blog')
    highlighted = models.TextField()

    class Meta:
        ordering = ('created',)

