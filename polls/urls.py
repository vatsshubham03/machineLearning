from django.urls import path
# from .views import index

from . import  views
urlpatterns = [
    path('',views.index),
    path('form',views.form),
    path('login',views.login)
]