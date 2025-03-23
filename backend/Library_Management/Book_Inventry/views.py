from datetime import date
from django.shortcuts import render

# rest_framework
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR
from django.shortcuts import get_object_or_404
from rest_framework.views import Response, status
from django.utils import timezone
from django.db import transaction

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

@api_view(['PUT'])
def update_book(request, pk):
    """
    Update an existing book and its image.
    """
    try:
        book = get_object_or_404(Books, pk=pk)
    except Books.DoesNotExist:
        return Response({"error": "Book not found."}, status=status.HTTP_404_NOT_FOUND)

    try:
        with transaction.atomic():
            # --- Update Book Details ---
            data = request.data

            # Use .get() with defaults for optional fields.  Handle partial updates correctly.
            book.book_name = data.get('book_name', book.book_name)
            book.book_author = data.get('book_author', book.book_author)
            book.book_description = data.get('book_description', book.book_description)
            book.book_price = data.get('book_price', book.book_price)
            book.book_updated_at = timezone.now()  # Use timezone.now() for updated_at

            # Don't update book_id (primary key) or book_created_at
            # book.book_id = data.get('book_id', book.book_id) #NO, DON'T UPDATE PRIMARY KEY
            # book.book_created_at = data.get('book_created_at',book.book_created_at)  #NO, keep original creation date

            # --- Update Image (Optional) ---
            image_data = request.FILES.get('book_image')  # Get the new image (if any)

            if image_data:
                # File size check (optional, but recommended)
                if image_data.size > 10 * 1024 * 1024:  # 10MB limit
                    return Response({"error": "Image file too large."}, status=status.HTTP_400_BAD_REQUEST)

                # Option 1: Replace the existing image (recommended).
                try:
                    book_image = BookImage.objects.get(book=book)  # Get the *existing* image
                    book_image.image = image_data  # Update the image field
                    book_image.save()
                except BookImage.DoesNotExist:  # Handle case where book has no image yet
                    BookImage.objects.create(book=book, image=image_data)  # Create a new image
                    
                #option 2: Delete and recreate (not recommended, use Option 1)
                # BookImage.objects.filter(book=book).delete()
                # BookImage.objects.create(book=book, image=image_data)

            # --- Save and Return Updated Data ---
            book.save()

            # Fetch and serialize the updated book and image.
            updated_book = get_object_or_404(Books, pk=pk) # Refetch

            book_serializer = AllBookInfoSerializers(updated_book)
            book_images = BookImage.objects.filter(book=updated_book)
            image_serializer = BookImageSerializer(book_images, many=True)

            book_data = book_serializer.data
            book_data['images'] = image_serializer.data

            return Response(book_data, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_book_by_id(request, pk):
  """
  Retrieve a book by its ID, including its image.
  """
  try:
    book = get_object_or_404(Books, pk=pk)  # Use get_object_or_404

    # Serialize the book data
    book_serializer = AllBookInfoSerializers(book)

    # Get and serialize the associated image(s)
    images = BookImage.objects.filter(book=book)
    image_serializer = BookImageSerializer(images, many=True)

    # Combine book and image data
    book_data = book_serializer.data
    book_data['images'] = image_serializer.data

    return Response(book_data, status=status.HTTP_200_OK)

  except Exception as e:
    # This is good practice to catch any other unexpected errors
    return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
