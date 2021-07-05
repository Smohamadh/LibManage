from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from LMapp.models import Author, Publisher, Book
from LMapp.serializers import AuthorModelSerializer, PublisherModelSerializer, BookModelSerializer


class GetAllBooks(APIView):

    def get(self, request):
        query = Book.objects.all()
        serialize = BookModelSerializer(query, many=True)
        return Response(serialize.data, status=status.HTTP_200_OK)


class GetAllAuthors(APIView):

    def get(self, request):
        query = Author.objects.all()
        serialize = AuthorModelSerializer(query, many=True)
        return Response(serialize.data, status=status.HTTP_200_OK)


class GetAllPublishers(APIView):

    def get(self, request):
        query = Publisher.objects.all()
        serialize = PublisherModelSerializer(query, many=True)
        return Response(serialize.data, status=status.HTTP_200_OK)


class PostModelBook(APIView):

    def post(self, request):
        serialize = BookModelSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_201_CREATED)
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)


class SearchBooksFromAuthor(APIView):

    def get(self, request):
        search = request.GET['id']
        query = Book.objects.filter(authors=search)
        serialize = BookModelSerializer(query, many=True)
        return Response(serialize.data, status=status.HTTP_200_OK)


class SearchBooksFromPublisher(APIView):

    def get(self, request):
        search = request.GET['name']
        change_to_id = Publisher.objects.get(name__contains=search).id
        query = Book.objects.filter(publisher=change_to_id)
        serialize = BookModelSerializer(query, many=True)
        return Response(serialize.data, status=status.HTTP_200_OK)
