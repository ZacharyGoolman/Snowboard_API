from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SnowboardSerializer
from .models import Snowboard

@api_view(['GET', 'POST'])
def snowboards_list(request):


    if request.method == 'GET':
        snowboards = Snowboard.objects.all()
        serializer = SnowboardSerializer(snowboards, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SnowboardSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT'])
def snowboard_detail(request, pk):
    snowboard = get_object_or_404(Snowboard, pk=pk)
    if request.method == 'GET':
        serializer = SnowboardSerializer(snowboard);
        return Response(serializer.data)
    elif request.method == 'PUT':
        
        serializer = SnowboardSerializer(snowboard, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
       
   