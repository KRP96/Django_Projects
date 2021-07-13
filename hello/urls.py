from django.urls import path

from. import views         #import views.py

urlpatterns = [
    path("", views.index, name="index"),    #first arguments is "" empty and second argument is function name index in views.py  URL=http://127.0.0.1:8000/hello/
    path("<str:name>", views.greet, name="greet"),  #we can use any name with that. ex : http://127.0.0.1:8000/hello/Kavinda   output==> Hello, Kavinda!
    path("brian", views.brian, name="brian"), #Added new line URL=http://127.0.0.1:8000/hello/brian
    path("david", views.david, name= "david") ,   #URL=http://127.0.0.1:8000/hello/david                
]