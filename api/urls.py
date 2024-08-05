from home.views import index, createPeople, updatePeoplePut, updatePeoplePatch, deletePeople ,particularIndex, RegisterApi, LoginApi
from django.urls import path,include
from products.views import ProductsApi
from peoples.views import PeoplesViewSet
from rest_framework.routers import DefaultRouter
from items.views import register_user

router = DefaultRouter()
router.register(r'peoples', PeoplesViewSet, basename='people')

urlpatterns = [
    path('',include(router.urls)),
    path('index/', index),
    path('index/<int:id>/', particularIndex),
    path('create-people/', createPeople),
    path('update-people-put/', updatePeoplePut),
    path('update-people-patch/', updatePeoplePatch),
    path('delete-people/', deletePeople),
    path('product-api/', ProductsApi.as_view()), 
    path('product-api/<int:pk>/', ProductsApi.as_view()), 
    path('register/',RegisterApi.as_view()),
    path('login/', LoginApi.as_view()),
    path('register-user',register_user)
]
