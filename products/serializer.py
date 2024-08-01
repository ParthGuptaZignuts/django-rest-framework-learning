import re
from rest_framework import serializers
from .models import Products

class ProuductsSerializers(serializers.ModelSerializer) :
    class Meta :
        model = Products
        fields = "__all__"

    def validate_products_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("Product title cannot be empty.")
    
        if not re.match(r'^[A-Za-z\s]+$', value):
            raise serializers.ValidationError("Product title cannot contain special characters or numbers.")

        return value