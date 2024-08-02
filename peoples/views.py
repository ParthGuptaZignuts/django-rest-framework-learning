from django.shortcuts import render

from rest_framework import viewsets
from .models import Peoples
from .serializers import PeopleSerializer

class PeoplesViewSet(viewsets.ModelViewSet):
    queryset = Peoples.objects.all()
    serializer_class = PeopleSerializer