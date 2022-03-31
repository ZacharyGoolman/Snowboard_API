from dataclasses import fields
from rest_framework import serializers
from .models import Snowboard

class SnowboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snowboard
        fields = ['id', 'title', 'description', 'price', 'inventory_quantity']