import re
from rest_framework import serializers
from .models import Person

class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"

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
