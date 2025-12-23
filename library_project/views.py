from django.shortcuts import render
from .models import Books
from .serializers import BookSerializer

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class BookListApiView(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer

# Bu API qanday ishlashini ko'rsatish uchun oddiy misol Bu BookListApiView si uchun misol
# class BookListApiView(APIView):
#     def get(self, request):
#         books = Books.objects.all()
#         print(books)
#         serializer = BookSerializer(books, many=True).data
#         data = {
#             "status": f"{len(books)} books found",
#             "books": serializer           
#                 }   
#         return Response(data)



class BookCreateApiView(generics.CreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    
# Bu API qanday ishlashini ko'rsatish uchun oddiy misol Bu BookCreateApiView si uchun misol
# class BookCreateApiView(APIView):
#     def post(self, request):
#         data = request.data
#         serializer = BookSerializer(data=data)
        
#         if serializer.is_valid():
#             serializer.save()
#             data = {
#                 "status": "success",
#                 "book": serializer.data
#             }
#             return Response(data) 
#         else:
#             data = {
#                 "status": "error",
#                 "errors": serializer.errors
#             }
#             return Response(data, status=400)
 
 
 
 
class BookDetailApiView(generics.RetrieveAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    
# Bu API qanday ishlashini ko'rsatish uchun oddiy misol Bu BookDetailApiView si uchun misol
# class BookDetailApiView(APIView):
#     def get(self, request, pk):
#         try:
#             book = Books.objects.get(pk=pk)
#             serializer = BookSerializer(book).data
#             data = {
#                 "status": "success",
#                 "book": serializer
#             }
#             return Response(data)
#         except Books.DoesNotExist:
#             data = {
#                 "status": "error",
#                 "message": "Book not found"
#             }
#             return Response(data, status=404)    
    
    
    
    
    
class BookDeleteApiView(generics.DestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    
    
class BookUpdateApiView(generics.UpdateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer    

# Efficient way to create CRUD API views using Django REST Framework's generic views

class BookListCreateApiView(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    
class BookDeleteUpdateApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer    
    
    


# Yuqoridagi hamma viewlar bitta viewsetda
class BookViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    # crud uchun asosan create,retrieve,update,delete uchun