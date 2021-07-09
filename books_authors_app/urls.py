from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('books', views.books),
    path('authors', views.publisher),
    path('book/<int:num>', views.book),
    path('author/<int:num>', views.author),
    path('addbook', views.createbook),
    path('addauthor', views.createauthor),
    path('books/<int:num>', views.updatebook),
    path('authors/<int:num>/update', views.updateauthor),

]
