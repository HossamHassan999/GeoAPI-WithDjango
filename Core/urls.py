
from django.urls import path 
from .views import *

urlpatterns = [
    
    path('Building/', BuildingAPIView.as_view(), name='Building'),
    path('BuildingDetailsAPIView/<int:id>/', BuildingDetailsAPIView.as_view(), name='BuildingDetailsAPIView')
    
]