from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *


class RegistrationSerializer(serializers.ModelSerializer):
     class Meta:
        model = User
        fields = [
            "id", 
            "username", 
            "first_name", 
            "last_name", 
            "email", 
            "password"
        ]
        extra_kwargs = {"id": {"read_only": True}, "password": {"write_only": True}}

def create(self, validated_data):
    username = validated_data["username"]
    first_name = validated_data["first_name"]
    last_name = validated_data["last_name"]
    email = validated_data["email"]
    password = validated_data["password"]

    user = User.objects.create_user(
        username=username,
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=password,
    )
    return user

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    author = serializers.StringRelatedField()

    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'content', 'image', 'owner')

class CommentSerializer(serializers.ModelSerializer):
    post = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = ('id', 'post', 'commented_by', 'body', 'created_on')

class UserSerializer(serializers.ModelSerializer):
    connect_app = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Post.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'connect_app')
