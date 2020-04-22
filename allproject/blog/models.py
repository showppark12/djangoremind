from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField('date published')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]