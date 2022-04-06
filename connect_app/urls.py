from django.urls.conf import path
from .views import *
from rest_framework.authtoken.views import obtain_auth_token
from connect_app import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("/api-token-auth", UserView.as_view()),
    path("/api-register-auth", RegistrationView.as_view()),
    # path("/api-token-auth", obtain_auth_token.as_views()),
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view()),
    path('comments/', views.CommentList.as_view()),
    path('comments/<int:pk>/', views.CommentDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)