from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from home.serializer import PeopleSerializer, CustomSerializer , RegisterSerializer , LoginSerializer
from home.models import Person
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

class RegisterApi(APIView):
    def post(self, request):
      data = request.data 
      serialized_data = RegisterSerializer.serialize(data=data)

      if not serialized_data.is_valid():
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
      return Response(serialized_data.validated_data, status=status.HTTP_201_CREATED)

class LoginApi(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def login(request):
    data = request.data
    serialized_data = CustomSerializer.serialize(data=data)
    if serialized_data.is_valid():
        return Response({"message": "success"}, serialized_data.validated_data, status=status.HTTP_200_OK)
    return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def index(request):
    data = Person.objects.all()
    serialized_data = PeopleSerializer(data, many=True)
    return Response(serialized_data.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def particularIndex(request, id):
    # Use the id passed as a URL parameter
    person = get_object_or_404(Person, id=id)
    serialized_data = PeopleSerializer(person)
    return Response(serialized_data.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createPeople(request):
    serializer = PeopleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def updatePeoplePatch(request):
    person = get_object_or_404(Person, id=request.data.get('id'))
    serializer = PeopleSerializer(person, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def updatePeoplePut(request):
    person = get_object_or_404(Person, id=request.data.get('id'))
    serializer = PeopleSerializer(person, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deletePeople(request):
    person = get_object_or_404(Person, id=request.data.get('id'))
    person.delete()
    return Response({"message": "Person deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
