from rest_framework import serializers
from LMapp.models import Book, Publisher, Author


class AuthorModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = '__all__'


class PublisherModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Publisher
        fields = '__all__'


class BookModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'
