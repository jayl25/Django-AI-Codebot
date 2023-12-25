
from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.LoginUser.as_view(), name="login"),
    path('register/', views.SignUp.as_view(), name="register"),
    path('logout/', views.LogoutUser.as_view(), name="logout"),
]