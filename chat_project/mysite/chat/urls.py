# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('users/<str:username>/group',views.updateGroupForUser),
]
