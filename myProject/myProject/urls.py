from django.contrib import admin
from django.urls import path,include
from django.views.defaults import server_error

from .views import bonjour, vue_de_test

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("myApp.urls")),
    path('bonjour/',server_error),
    path('bonjours/',bonjour,name="bonjour"),
    path('test/',vue_de_test,name="index"),

]
