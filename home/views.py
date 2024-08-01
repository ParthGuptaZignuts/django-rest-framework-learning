from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from home.serializer import PeopleSerializer
from home.models import Person
from django.shortcuts import get_object_or_404

@api_view(['GET'])
def index(request):
    data = Person.objects.all()
    serialized_data = PeopleSerializer(data, many=True)
    return Response(serialized_data.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def createPeople(request):
    serializer = PeopleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
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
def deletePeople(request):
    person = get_object_or_404(Person, id=request.data.get('id'))
    person.delete()
    return Response({"message": "People deleted successfully"},status=status.HTTP_204_NO_CONTENT)
