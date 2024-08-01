from home.views import index, createPeople, updatePeoplePut, updatePeoplePatch, deletePeople ,particularIndex
from django.urls import path
from products.views import ProductsApi

urlpatterns = [
    path('index/', index),
    path('index/<int:id>/', particularIndex),
    path('create-people/', createPeople),
    path('update-people-put/', updatePeoplePut),
    path('update-people-patch/', updatePeoplePatch),
    path('delete-people/', deletePeople),
    path('product-api/', ProductsApi.as_view()), 
    path('product-api/<int:pk>/', ProductsApi.as_view()), 
]
