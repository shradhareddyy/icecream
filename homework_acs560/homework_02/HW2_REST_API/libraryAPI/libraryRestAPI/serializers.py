from .models import books
from rest_framework import serializers

class librarySerializer (serializers.ModelSerializer):
    class Meta:
        model = books
        fields = '__all__'
