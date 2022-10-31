from django.urls import path , include
from . import views

urlpatterns = [
    path('index_test',views.go_index),
]