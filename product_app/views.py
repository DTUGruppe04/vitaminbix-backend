from django.http import JsonResponse, HttpResponse
from django.utils import timezone
import json
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from product_app.models import Book


# Create your views here.

# Simple HelloWorld Endpoint Response
def hello_view(request):
    return JsonResponse({"message": "Hello Frontend. This data came from the backend. Nice to see you"})


# Add a book with POST Request
@csrf_exempt
def add_book(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        book = Book(title=data['title'], author=data['author'], publication_date=timezone.now())
        book.save()
        return HttpResponse('Book added successfully!')
    else:
        return HttpResponse('Invalid Request', status=400)


# Return all books from a database as JSON
def get_books(request):
    books = Book.objects.all()
    book_list_serialized = serializers.serialize('json', books)
    return JsonResponse(book_list_serialized, safe=False)
