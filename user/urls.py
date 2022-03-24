from django.urls import path
from django.urls.conf import include
from . import views


urlpatterns = [
    path('',views.index),
    path('reg',views.reg),
    path('login',views.login),
    path('admin',views.admin),
    path('emp',views.emp)
]
