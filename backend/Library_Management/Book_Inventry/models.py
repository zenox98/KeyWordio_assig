import os
from django.db import models

def book_image_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/item_images/<item_id>/<filename>
    return os.path.join('book_images', str(instance.book.book_id), filename)

class Books(models.Model):
  book_id = models.CharField(primary_key=True, max_length=30)
  book_name = models.CharField(max_length=100)
  book_author = models.CharField(max_length=100)
  book_price = models.DecimalField(max_digits=10, decimal_places=2)
  book_description = models.TextField()
  book_created_at = models.DateTimeField(auto_now_add=True)
  book_updated_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.book_name

class BookImage(models.Model) :
  book = models.ForeignKey(Books, on_delete=models.CASCADE, to_field="book_id")
  image = models.ImageField(upload_to=book_image_path) # Use custom upload path
  created_at = models.DateTimeField(auto_now_add=True)
