from django.contrib.gis.db import models

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Building(models.Model):
    id = models.AutoField(primary_key=True)
    
    name = models.CharField(max_length=255)
    
    price = models.DecimalField(max_digits=10, decimal_places=2)  
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  
    
    geom = models.MultiPolygonField(srid=4326, spatial_index=True)  

    def __str__(self):
        return self.name
