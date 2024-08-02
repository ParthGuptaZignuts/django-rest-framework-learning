from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Peoples
from .serializers import PeopleSerializer

class PeoplesViewSet(viewsets.ModelViewSet):
    queryset = Peoples.objects.all()
    serializer_class = PeopleSerializer

    def list(self, request, *args, **kwargs):
        search_param = request.query_params.get('search', None)
        queryset = self.get_queryset()

        if search_param:
            queryset = queryset.filter(name__icontains=search_param)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
