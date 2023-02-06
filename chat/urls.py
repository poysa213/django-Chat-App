from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("chat/<str:chat_box_name>/", views.chat_box, name="chat"),
]