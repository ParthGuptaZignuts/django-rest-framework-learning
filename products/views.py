from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from products.models import Products
from products.serializer import ProuductsSerializers

class ProductsApi(APIView):
    def get(self, request, pk=None):
        if pk:
            product = get_object_or_404(Products, pk=pk)
            serialized_data = ProuductsSerializers(product)
        else:
            products = Products.objects.all()
            serialized_data = ProuductsSerializers(products, many=True)
        return Response(serialized_data.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProuductsSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        product = get_object_or_404(Products, pk=pk)
        serializer = ProuductsSerializers(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        product = get_object_or_404(Products, pk=pk)
        serializer = ProuductsSerializers(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = get_object_or_404(Products, pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
