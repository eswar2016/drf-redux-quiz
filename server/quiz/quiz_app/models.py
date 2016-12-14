from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Question(models.Model):
    question = models.CharField(max_length=300)
    answer = models.CharField(max_length=300)

    def __str__(self):
        return self.question