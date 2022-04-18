from django.db import models


class Joke(models.Model):

    category = models.CharField(max_length=20)
    joke = models.TextField()
    answer = models.TextField()
    source = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        unique_together = (('joke', 'answer'), )

