from django.db import models

class Options(models.Model):
    upper = models.BooleanField(default=False)
    lower = models.BooleanField(default=False)
    numbers = models.BooleanField(default=True)

