from django.db import models

# Create your models here.
class Geo(models.Model):
    lat = models.CharField(max_length=50)
    lon = models.CharField(max_length=50)
    place = models.TextField()
    date = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'geos'