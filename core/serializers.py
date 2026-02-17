from rest_framework import serializers
from .models import Role, Resource, Action, Permission

class RoleSerializer(serializers.ModelSerializer):
    class Meta: model = Role; fields = '__all__'

class ResourceSerializer(serializers.ModelSerializer):
    class Meta: model = Resource; fields = '__all__'

class ActionSerializer(serializers.ModelSerializer):
    class Meta: model = Action; fields = '__all__'

class PermissionSerializer(serializers.ModelSerializer):
    class Meta: model = Permission; fields = '__all__'
