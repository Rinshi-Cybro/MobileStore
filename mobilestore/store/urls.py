from django.urls import path
from .views import *

urlpatterns = [
    path('shome/',StoreHome.as_view(),name='shome'),
    path('addprdt/',AddprdView.as_view(),name='addprdt'),
    path('viewprdt/',ProdView.as_view(),name='viewprdt'),
    path('deltprdt<int:did>',DeleteProdct.as_view(),name='deltprdt'),
    path('editprdt<int:did>',EditProduct.as_view(),name='editprdt'),
    
]
