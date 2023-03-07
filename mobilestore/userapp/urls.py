from django.urls import path
from .views import *

urlpatterns = [
    path('uhome/',UserHome.as_view(),name='uhome'),
    path('prodview/',ProductView.as_view(),name='prodview'),

]