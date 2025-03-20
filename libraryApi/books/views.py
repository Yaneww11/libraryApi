from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, ListCreateAPIView, \
    RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from libraryApi.books.models import Book, Publisher
from libraryApi.books.permissions import IsBookOwner
from libraryApi.books.serializers import BookSerializer, PublisherHyperlinkedSerializer, PublisherSerializer, \
    SimpleBookSerializer


class ListBookView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

@extend_schema(
    request=BookSerializer,
    responses={201: BookSerializer, 400: BookSerializer}
)
# class DetailBookView(APIView):
#
#     @staticmethod
#     def serializer_valid(serializer):
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def get(self, request, pk):
#         book = Book.objects.get(pk=pk)
#         serializer = BookSerializer(book)
#         return Response({"book":serializer.data})
#
#     def put(self, request, pk):
#         book = Book.objects.get(pk=pk)
#         serializer = BookSerializer(book, data=request.data)
#         return self.serializer_valid(serializer)
#
#     def patch(self, request, pk: int):
#         book = Book.objects.get(pk=pk)
#         serializer = BookSerializer(book, data=request.data, partial=True)
#         return self.serializer_valid(serializer)
#
#     def delete(self, request, pk):
#         book = Book.objects.get(pk=pk)
#         book.delete()
#         return Response(status=status.HTTP_200_OK)


class DetailBookView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = SimpleBookSerializer
    permission_classes = [IsBookOwner]
    authentication_classes = [TokenAuthentication]


def demo(request):
    return render(request, 'demo.html')


class PublisherViewSet(ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class PublisherHyperLinkedView(ListAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherHyperlinkedSerializer