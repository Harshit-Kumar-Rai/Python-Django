from django.db import models

class Data(models.Model):
    
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name
