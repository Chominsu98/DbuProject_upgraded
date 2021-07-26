from django.db import models

# Create your models here.
class Passcode(models.Model):
    passcode=models.CharField(max_length=128)
   
    def __str__(self):
        return self.passcode