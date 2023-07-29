# books/urls.py
from . import views
from django.urls import path
# from .views import book_list, create_book, get_book, update_book, delete_book

# urlpatterns = [
#     path('books/', book_list, name='book-list-create'),
#     path('books/<int:pk>/', get_book, name='book-retrieve-update-delete'),
#     path('books/create/', create_book, name='book-create'),
#     path('books/<int:pk>/update/', update_book, name='book-update'),
#     path('books/<int:pk>/delete/', delete_book, name='book-delete'),
# ]

urlpatterns = [
    # path('', views.add, name = "add"),
     path('', views.renderform, name = "form"),

]