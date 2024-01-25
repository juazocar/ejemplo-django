from django.urls import path
from . import views


urlpatterns = [
    path('menu', views.menu, name='menu'),
    path('quienes-somos', views.quienes_somos, name='quienes-somos'),

   ]