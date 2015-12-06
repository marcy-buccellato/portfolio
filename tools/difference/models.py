from django.db import models


class Difference(models.Model):
    number = models.IntegerField(default=0, primary_key=True)
    value = models.IntegerField(default=0)
    occurrences = models.IntegerField(default=0)
    update_dt = models.DateTimeField(auto_now=True)
