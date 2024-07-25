from rest_framework import serializers
from .models import User

class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    uid = serializers.CharField(max_length=100)
    name = serializers.CharField(max_length=100)
    bio = serializers.CharField(max_length=300, required=False, allow_blank=True)
    category = serializers.CharField(max_length=100, required=False, allow_blank=True)
    followers = serializers.IntegerField(required=False, default=0)
    posts = serializers.IntegerField(required=False, default=0)    

    def create(self, validated_data):
        return User(**validated_data)