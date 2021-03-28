from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Book

# Create your views here.


def index(request):
    return render(request, 'ajax_1/index.html')


def book_add(request):
    name = request.GET['book_name']
    price = request.GET['book_price']
    page = request.GET['book_page']
    book = Book(name=name, price=price, pages=page)
    try:
        book.save()
        return HttpResponse('Book Added Successfully')
    except:
        return HttpResponse('Error')
