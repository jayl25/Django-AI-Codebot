from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('ask/', views.ask, name="ask"),
    path('previous/', views.previously_asked, name="previous"),
]