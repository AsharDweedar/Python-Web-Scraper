from django.db import models

# Create your models here.
class Dashbord(models.Model):
    title = models.CharField(max_length=100, null=False)
    content = models.CharField(max_length=4000, null=False)
    url = models.CharField(max_length=400, null=True, blank=True)

    def __unicode__(self):
        return self.title