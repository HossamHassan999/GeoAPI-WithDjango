from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Building
from .serializers import BuildingSerializer

class BuildingAPIView(APIView):

    def get(self, request):
        buildings = Building.objects.all()
        serializer = BuildingSerializer(buildings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BuildingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BuildingDetailsAPIView(APIView):

    def get(self, request, id):
        building = get_object_or_404(Building, id=id)
        serializer = BuildingSerializer(building)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        building = get_object_or_404(Building, id=id)
        serializer = BuildingSerializer(building, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        building = get_object_or_404(Building, id=id)
        building.delete()
        return Response({"message": "Building deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
