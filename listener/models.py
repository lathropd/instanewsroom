from django.db import models

class Heard(models.Model):
    payload = models.TextField(blank=True)
