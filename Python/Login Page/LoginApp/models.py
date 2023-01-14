from django.db import models

class user(models.Model):
    username = models.CharField(max_length=20, null=False)
    password = models.CharField(max_length=8, null=False)
    
    def __str__(self):
        return self.username