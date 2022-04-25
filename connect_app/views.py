from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from connect_app.serializers import CommentSerializer, PostSerializer, RegistrationSerializer, UserSerializer
from rest_framework import serializers, generics, status, permissions
from rest_framework.authtoken.models import Token
from .models import *
from .permissions import IsOwnerOrReadOnly


class UserView(APIView):
    permissions_classes = [IsAuthenticated]

    def get(self, request):
        context = {"message": "Hello, World!"}
        return Response(context)


class RegistrationView(APIView):
    def post(self, request, *args, **kwargs):
        registration_serializer = RegistrationSerializer(data=request.data)

        for user in User.objects.all():
            if not user:
                break
            else:
                try:
                    Token.objects.get(user_id=user.id)
                except Token.DoesNotExist: 
                    Token.objects.create(user=user)

        if registration_class.is_valid():
            user = registration_serializer.save()
            token = Token.objects.create(user=user)

            return Response(
                {
                    "user": {
                        "id": serializers.data["id"],
                        "first_name": serializers.data["first_name"],
                        "last_name": serializers.data["last_name"],
                        "username": serializers.data["username"],
                        "email": serializers.data["email"],
                    },
                    "token": token.key,
                }
            )
        return Response(
            {
                "error": serializers.errors,
                "status": f"{status.HTTP_203_NON_AUTHORITATIVE_INFORMATION} \
                    NON AUTHORITATIVE INFORMATION",
            }
        )

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)
    

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView): 
    queryset = User.objects.all()
    serializer_class = UserSerializer






