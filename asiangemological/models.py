from django.db import models

class Stone(models.Model):
    verification_number = models.CharField(max_length=30)

    def __str__(self):
        return self.verification_number