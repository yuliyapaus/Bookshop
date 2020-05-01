from django.urls import re_path, path
from bookshop import views

urlpatterns = [
        path("api/v1/list/", views.BookListView.as_view()),
        path("api/v1/create/", views.BookCreateView.as_view()),
        path("api/v1/update/<int:pk>/", views.BookDetailView.as_view()),
        re_path(r'^$', views.hello),
        re_path(r"^world/$", views.world, name = "world_page"),
        re_path(r"^just_url/(?P<id_book>[\d]+)/$", views.comment_handler, name = "comment_url"),

        ]
