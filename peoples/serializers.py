from rest_framework import serializers
from .models import Peoples
import re

class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Peoples
        fields = ['name', 'age', 'email']
    
    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Name cannot be empty.")
        if not re.match(r'^[A-Za-z\s]+$', value):
            raise serializers.ValidationError("Name cannot contain special characters or numbers.")
        return value

    def validate_age(self, value):
        if value < 0:
            raise serializers.ValidationError("Age cannot be negative.")
        return value