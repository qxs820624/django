from rest_framework import serializers

from .models import Package

class PackageSerializer(serializers.ModelSerializer):
    """package serializer"""
    owner = serializers.ReadOnlyField(source = 'user_id.username')
    class Meta:
        model = Package
        fields = ['name','status','owner']


class PackageallSerializer(serializers.ModelSerializer):
    """package serializer"""
    class Meta:
        model = Package
        fields = ['name','status']
