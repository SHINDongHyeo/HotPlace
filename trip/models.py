from django.db import models

class InstaHP(models.Model):
    location = models.CharField(max_length=15)

    def __str__(self):
    	return self.location
