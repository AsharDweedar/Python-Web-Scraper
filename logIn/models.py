from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=120,null=False)
    password = models.CharField(max_length=120,null=False)

    def __unicode__(self): 
        return self.name