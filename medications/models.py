from django.db import models

class Medication(models.Model):
    name = models.CharField(max_length=200)
    is_otc = models.BooleanField(default=False)

    def __str__(self):
        return self.name