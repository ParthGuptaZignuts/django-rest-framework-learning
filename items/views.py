from django.shortcuts import render
from .models import Items,Insaan
from rest_framework.decorators import api_view,permission_classes
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


@api_view(['POST'])
def register_user(request):
    data = request.data
    try:
        user = Insaan.objects.create_user(
            username = data['username'],
            password = data['password'],
            email    = data['email']
        )
        return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)



