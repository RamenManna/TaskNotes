from cgitb import html
from turtle import update
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="list"),
    path('update.html/<str:pk>/',views.updateTask,name="update"),
    path('delete.html/<str:pk>/',views.deleteTask,name="delete"),
]
