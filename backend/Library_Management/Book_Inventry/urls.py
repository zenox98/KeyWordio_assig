from re import DEBUG
from django.urls import path
from django.conf import settings
from django.conf.urls import static
from . import views

app_name = 'Book_Inventry'

urlpatterns = [
  path('list_books/', views.list_books, name='list_books'),
  path('add_book/', views.add_book, name='add_book'),
  path('delete_book/<str:book_id>', views.delete_book, name='delete_book'),
  path('update_book/<str:book_id>', views.update_book, name='update_book'),
  path('get_book_by_id/<str:pk>', views.get_book_by_id, name='get_book_by_id'),  # Add this line
]

if DEBUG:
    urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
