from django.db import models

# Create your models here.
class YTClist(models.Model):
    url=models.CharField(max_length=150)
    def __str__(self):
        return self.url