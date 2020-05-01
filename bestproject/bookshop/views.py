from django.shortcuts import render, redirect
from django.http import HttpResponse
from bookshop import models
from bookshop.forms import CommentForm
from bookshop.task import test_fun
import logging
from bookshop.serializer import BookSerializer, BookSerializerCreate
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from bookshop.models import Book



logger = logging.getLogger('django')
promise = None

def hello(request):
    #logger.error('hello error')
    global promise
    promise = test_fun.delay(10)
    
    return HttpResponse("<h2>Hello from Django </h2>")

def world(request):
    response = {}
    #global promise
    if getattr(promise, "state", False) != "PENDING":
        response = {"promise": promise.get()}
    
    response['all_books'] =  models.Book.objects.all()
    response['comment'] = CommentForm()
    return render(request, './bookshop/index.html', response)

def comment_handler(request, id_book):
    form = CommentForm(request.POST)
    
    
    if form.is_valid():
        obj = form.save(commit=False)
        obj.comment_book_id = id_book
        obj.save()
        return redirect('world_page')
    return HttpResponse('error')

class BookListView(ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class BookCreateView(CreateAPIView):
    serializer_class = BookSerializerCreate

class BookDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializerCreate
    queryset = Book.objects.all()

