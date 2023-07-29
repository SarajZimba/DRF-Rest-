from django.shortcuts import render
from django.http import HttpResponse
import requests
from .forms import Item1Form
from .forms import CreateUserForm
# # Create your views here.

# # books/views.py

# from django.http import JsonResponse
# from .models import Book
# from django.views.decorators.http import require_GET, require_POST

# @require_GET
# def book_list(request):
#     books = Book.objects.all()
#     data = [{'id': book.id, 'title': book.title, 'author': book.author, 'published_year': book.published_year, 'isbn': book.isbn} for book in books]
#     return JsonResponse(data, safe=False)

# @require_POST
# def create_book(request):
#     data = {
#         'title': request.POST['title'],
#         'author': request.POST['author'],
#         'published_year': request.POST['published_year'],
#         'isbn': request.POST['isbn']
#     }
#     book = Book.objects.create(**data)
#     return JsonResponse({'id': book.id, 'title': book.title, 'author': book.author, 'published_year': book.published_year, 'isbn': book.isbn})

# @require_GET
# def get_book(request, pk):
#     try:
#         book = Book.objects.get(id=pk)
#         data = {'id': book.id, 'title': book.title, 'author': book.author, 'published_year': book.published_year, 'isbn': book.isbn}
#         return JsonResponse(data)
#     except Book.DoesNotExist:
#         return JsonResponse({'error': 'Book not found'}, status=404)

# @require_POST
# def update_book(request, pk):
#     try:
#         book = Book.objects.get(id=pk)
#         data = {
#             'title': request.POST['title'],
#             'author': request.POST['author'],
#             'published_year': request.POST['published_year'],
#             'isbn': request.POST['isbn']
#         }
#         for key, value in data.items():
#             setattr(book, key, value)
#         book.save()
#         return JsonResponse({'id': book.id, 'title': book.title, 'author': book.author, 'published_year': book.published_year, 'isbn': book.isbn})
#     except Book.DoesNotExist:
#         return JsonResponse({'error': 'Book not found'}, status=404)

# @require_POST
# def delete_book(request, pk):
#     try:
#         book = Book.objects.get(id=pk)
#         book.delete()
#         return JsonResponse({'message': 'Book deleted successfully'})
#     except Book.DoesNotExist:
#         return JsonResponse({'error': 'Book not found'}, status=404)

# def add(request):
#     print(2+4)
#     return HttpResponse("Hello Everybody")

# def div(a, b):
#     try:
#         c  = a/b;
#         print(f"The division is {c}")
#     except:
#         b=0;

def add(request):
    data = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    context = {"datas": data}
    return render(request, "home.html", context)


def renderform(request):
    form =CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'form.html', context = {"form": form})
