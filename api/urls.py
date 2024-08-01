from home.views import index,createPeople,updatePeoplePut,updatePeoplePatch,deletePeople
from django.urls import path

urlpatterns = [
    path('index/',index),
    path('create-people/',createPeople),
    path('update-people-put/',updatePeoplePut),
    path('update-people-patch/',updatePeoplePatch),
    path('delete-people/',deletePeople)
]

