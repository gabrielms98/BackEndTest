from django.db import models


class Finance(models.Model):
    year = models.IntegerField()
    situation = models.CharField(max_length=100)
    value = models.FloatField()
    type = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.year} - {self.situation} - {self.value} - {self.type}"
