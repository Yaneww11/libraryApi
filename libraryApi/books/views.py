from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from libraryApi.books.models import Book
from libraryApi.books.serializers import BookSerializer


@extend_schema(
    request=BookSerializer,
    responses={201: BookSerializer, 400: BookSerializer}
)
class ListBookView(APIView):
    def get(self, request):
        book = Book.objects.all()
        serializer = BookSerializer(book, many=True)
        return Response({"book":serializer.data})

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(
    request=BookSerializer,
    responses={201: BookSerializer, 400: BookSerializer}
)
class DetailBookView(APIView):
    @staticmethod
    def serializer_valid(serializer):
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(book)
        return Response({"book":serializer.data})

    def put(self, request, pk):
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(book, data=request.data)
        return self.serializer_valid(serializer)

    def patch(self, request, pk: int):
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(book, data=request.data, partial=True)
        return self.serializer_valid(serializer)

    def delete(self, request, pk):
        book = Book.objects.get(pk=pk)
        book.delete()
        return Response(status=status.HTTP_200_OK)

def demo(request):
    return render(request, 'demo.html')