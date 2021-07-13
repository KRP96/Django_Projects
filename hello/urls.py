from django.urls import path

from. import views         #import views.py

urlpatterns = [
    path("", views.index, name="index")                         #first arguments is "" empty and second argument is function name index in views.py
]