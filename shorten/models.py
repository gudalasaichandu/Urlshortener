from django.db import models


class url(models.Model):
    long_url = models.CharField(max_length=10000, null=True, unique=True)
    short_hash = models.CharField(max_length=10000, null=True, unique=True)
    count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.long_url
