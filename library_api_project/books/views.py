from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BookSerializer
from .models import Book
from rest_framework import status

#class Based Views Imports:
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404 # if it can't get an object


class BookList(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many = True)
        return Response(serializer.data, status = status. HTTP_208_ALREADY_REPORTED)

    def post(self, request):
        seializer = BookSerializer(data = request.data)
        seializer.is_valid(raise_exception = True)
        seializer.save()
        return Response(seializer.data, status = status.HTTP_201_CREATED)

















#****************************************************************************************************

# @api_view(['GET', 'POST'])
# def book_list(request):
#     if request.method == 'GET':
  
#         books = Book.objects.all()
#         books_filtered_genre_science = books.filter(genre = 'Science')
#         books_filtered_genre_fiction = books.filter(genre = 'Fiction')
#         books_science_serialized = BookSerializer(books_filtered_genre_science, many = True)
#         books_fiction_serialized = BookSerializer(books_filtered_genre_fiction, many = True)

#         # serializer = BookSerializer(books_filtered_genre_science, many = True)
#     #***************************************    
#     # You can make a custom key pair value    
#         custom_dictionary = {"Science" : books_science_serialized.data,
#                             "Fiction" : books_fiction_serialized.data, }
#     #***************************************
#         #serializer = BookSerializer(books, many = True)

#     elif request.method == 'POST':
#         print(request.data)
#         serializer = BookSerializer(data = request.data)

#         if serializer.is_valid():
#             serializer.save() 
#         return Response(serializer.data, status = status.HTTP_201_CREATED)
#     # return Response(serializer.data)
#     return Response(custom_dictionary, status = status.HTTP_418_IM_A_TEAPOT)

# @api_view(['GET'])
# def book_list(request):

#     if request.method == 'GET':
#         books = Book.objects.all()
#         books_filtered_genre_science = books.filter(genre = 'Science')
#         serializer = BookSerializer(books_filtered_genre_science, many = True)
#     return Response(serializer.data, status = status.HTTP_418_IM_A_TEAPOT)
    

