#serializers.py
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    def post(self, validated_data):
        user = User.objects.create_user(
            nickname=validated_data['nickname'],
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user
    class Meta:
        model = User
        fields = ['nickname', 'username', 'password']