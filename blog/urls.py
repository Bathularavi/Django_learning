from django.urls import path
from .views import post_list

urlpatterns = [
    path('api/posts/', post_list),
]