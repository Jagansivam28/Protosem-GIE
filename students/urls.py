
from django.contrib import admin
from django.urls import path
from students.views import *



urlpatterns = [
    path('',charts,name="home"),
    path('login/',login,name="login"),
    path('register/',register,name='register'),
    path("update_gie",hardware_iot,name="hardware_iot"),
    path("ai", ai, name="ai"),
    path("charts",charts,name="charts"),
    path("software", software, name="software"),
    path("product_design",product_design,name="product_design"),
    path("software_platforms",software_platforms,name="software_platforms"),
    path('programming',programming,name="programming"),
    path("intellectual_property",intellectual_property,name="intellectual_property"),
    path("innovation",innovation,name="innovation"),
    path("logout", logout_request, name="logout"),
    path("dummytask",dummytaskinit,name="dummytask")
]