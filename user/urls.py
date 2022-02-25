from django.urls import path
from django.urls.conf import include
from . import views


urlpatterns = [
    path('',views.index),
    path('index1',views.index1)''
    path('reg',views.index1)
]
