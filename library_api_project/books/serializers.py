from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        # fields = ['id', 'title', 'publisher', 'author', 'quantity', ]
        # I could write field like this
        fields = '__all__'