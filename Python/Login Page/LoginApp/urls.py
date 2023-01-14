from django.urls import path
from .views import index,  Home, user_logout
urlpatterns = [
    path('', index, name="home"),
    path("home7", Home, name="ho"),
    path("logout", user_logout, name="logout")
]
