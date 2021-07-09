from django.shortcuts import render, HttpResponse, redirect
from .models import *


def index(request):
    return render(request, 'index.html')

def books(request):
    context={
        'books': Book.objects.all(),
    }
    return render(request, 'libros.html', context)

def publisher(request):
    context={
        'authors': Publisher.objects.all(),
    }
    return render(request,'autores.html',context)

def book(request, num):
    book= Book.objects.get(id=num)
    context={
        'book': book,
        'authors': book.publishers.all(),
        'allauthors': Publisher.objects.all()
    }
    return render(request,'libro.html', context)

def author(request, num):
    author = Publisher.objects.get(id=num)
    context={
        'author': author,
        'books': author.books.all(), 
        'allbooks': Book.objects.all(),
    }
    return render(request,'autor.html', context)

def createbook(request):
    Book.objects.create(
        title=request.POST['title'],
        description=request.POST['description']
    )
    return redirect('/books')

def createauthor(request):
    Publisher.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        notas=request.POST['notes']
    )
    return redirect('/authors')

def updatebook(request, num):
    book= Book.objects.get(id=num)
    addauthor= request.POST['addauthor']
    addauthor = Publisher.objects.get(id=addauthor)
    book.publishers.add(addauthor) 
    book.save()
    return redirect(f'/books/{num}')

def updateauthor(request, num):
    author=Publisher.objects.get(id=num)
    addbook=request.POST['addbook']
    addbook = Book.objects.get(id=addbook)
    author.books.add(addbook)
    author.save()
    return redirect(f'/authors/{num}')