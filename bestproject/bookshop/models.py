from django.db import models
from requests import get, post, put, delete, patch
from json import loads

# Create your models here.

class Author(models.Model):
    class Meta:
        db_table = "author"
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

    name = models.CharField(
            max_length=150,
            db_index=True, 
            verbose_name="Имя",
            help_text="Введите имя автора")

    def __str__(self):
        return self.name

class Genre(models.Model):
    class Meta:
        db_table = "genre"
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

    name = models.CharField(max_length=150, db_index=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    class Meta:
        db_table = "Book"
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
    name = models.CharField(max_length=150, db_index=True)
    book_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    book_genre = models.ForeignKey(Genre, on_delete=models.CASCADE, default="1")
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        json = {
                "name" : "name",
                "book_author": "book_author"
                }
        post("https://uliy.ololosha.xyz/django/api/v1/create/", json=json)


class Comment(models.Model):
    class Meta:
        db_table = "Comment"
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    text = models.TextField()
    comment_book = models.ForeignKey(
            Book,
            on_delete=models.CASCADE,
            related_name="Comment")

    def __str__(self):
        return self.text[:10] + "..."
