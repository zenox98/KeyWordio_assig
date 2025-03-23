from rest_framework import serializers
from .models import BookImage, Books

class AllBookInfoSerializers(serializers.ModelSerializer):
  class Meta:
    model = Books
    fields = '__all__'

class BookImageSerializer(serializers.ModelSerializer):
  class Meta:
    model = BookImage
    fields = ('image', 'created_at')

class UpdateBookInfoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Books
    fields = ('book_id', 'book_name', 'book_author', 'book_price', 'book_description', 'book_created_at')

class AddBookSerializers(serializers.ModelSerializer):
  class Meta:
    model = Books
    fields = ('book_id', 'book_name', 'book_author', 'book_price', 'book_description', 'book_updated_at')
