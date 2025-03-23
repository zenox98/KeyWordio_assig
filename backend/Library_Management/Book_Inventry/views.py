from datetime import date
from django.shortcuts import render

# rest_framework
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR
from rest_framework.views import Response, status

from .models import BookImage, Books
from .serialization import AddBookSerializers, AllBookInfoSerializers, BookImageSerializer

# Create your views here.
@api_view(['GET'])
def list_books(request):
  """
  List all books or create a new book.
  """
  try:
    if request.method == 'GET':
      books = Books.objects.all()
      book_data = []

      for book in books:
        book_serializer = AllBookInfoSerializers(book)
        book_images = BookImage.objects.filter(book=book)
        image_serializer = BookImageSerializer(book_images, many=True)  # Serialize the images

        book_with_images = book_serializer.data
        book_with_images['images'] = image_serializer.data  # Add serialized image data
        book_data.append(book_with_images)

      return Response(book_data, status=HTTP_200_OK)
    else:
      Response(status=HTTP_404_NOT_FOUND)
  except Books.DoesNotExist:
    Response(status=HTTP_404_NOT_FOUND)
  except Exception:
    Response(status=HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def add_book(request):
  try:
    if request.method == 'POST':
      data = request.data
      book_name = data.get('book_name')
      book_id = data.get('book_id')
      book_author = data.get('book_author')
      book_description = data.get('book_description')
      book_price = data.get('book_price')
      book_created_at = data.get('book_created_at')
      book_image = data.get('book_image')

      book = Books.objects.create(
        book_id = book_id,
        book_name = book_name,
        book_description = book_description,
        book_author = book_author,
        book_price = book_price,
        book_created_at = book_created_at
      )

      bookImage = BookImage.objects.create(
        book  = book,
        image = book_image,
        created_at = date.today
      )

      book.save()
      bookImage.save()

      return Response({
        "message": "User created successfully!",
        "data": {
          "book" : book,
          "images" : bookImage
        }
      }, status=status.HTTP_201_CREATED)

  except Exception as e:  # Catch general exceptions during creation
    return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['DELETE'])
def delete_book(request, book_id):
  try:
    if request.method == 'DELETE':
      book = Books.objects.get(book_id=book_id)
      book.delete()
      return Response({"message": "Book deleted successfully"}, status=status.HTTP_200_OK)
    return Response({"error": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
  except Books.DoesNotExist:
    return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)
