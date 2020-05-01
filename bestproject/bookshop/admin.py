from django.contrib import admin
from bookshop.models import Author, Book, Genre, Comment

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Comment)

# Register your models here.
