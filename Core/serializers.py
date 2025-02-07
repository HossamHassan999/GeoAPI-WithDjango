from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework import serializers
from .models import Building

class BuildingSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Building
        geo_field = "geom"  
        fields = ( "name", "price", "category")  
