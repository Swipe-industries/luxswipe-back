from rest_framework import serializers
from .models import User

class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    uid = serializers.CharField(max_length=200)
    name = serializers.CharField(max_length=100)
    bio = serializers.CharField(max_length=500)

    def create(self, validated_data):
        return User(**validated_data)