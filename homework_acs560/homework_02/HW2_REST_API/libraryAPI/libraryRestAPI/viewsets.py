from rest_framework import viewsets
from . import models
from . import serializers

class BookViewSet(viewsets.ModelViewSet):
    queryset = models.books.objects.all()
    serializer_class = serializers.librarySerializer
    
