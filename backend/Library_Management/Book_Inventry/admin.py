from django.contrib import admin

# Register your models here.
from .models import Books, BookImage

class Book_InventryAdmin(admin.ModelAdmin):
  list_display = ('book_id', 'book_name', 'book_author', 'book_price', 'book_description')

admin.site.register(Books, Book_InventryAdmin)

class BookImageAdmin(admin.ModelAdmin):
  list_display = ('image', 'created_at')

admin.site.register(BookImage, BookImageAdmin)
