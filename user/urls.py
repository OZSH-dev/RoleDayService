from django.urls import path

from . import views

urlpatterns = [
    path('login', views.log_in, name='index'),
    path('auth', views.auth, name='auth'),
    path('logout', views.log_out, name='logout')
]