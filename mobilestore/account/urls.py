from django.urls import path
from .views import *

urlpatterns = [
    path('reg/',UserRegView.as_view(),name='reg'),
    path('log/',LoginView.as_view(),name='log'),
    path('logout/',SingOut.as_view(),name='logout'),                          

]
