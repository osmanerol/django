from django.urls import path
from account.views import ProfileView, UpdatePasswordAPIView, CreateUserView

urlpatterns = [
    path('me', ProfileView.as_view(), name= 'me'),
    path('change-password', UpdatePasswordAPIView.as_view(), name= 'change-password'),
    path('register', CreateUserView.as_view(), name= 'register'),
] 