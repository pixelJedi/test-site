import math

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from .models import Book, Genre


def count_pages(page, n):
    maxpage = math.ceil(Book.objects.count() / page)
    pages = [i for i in range(n - 2, n + 3) if (0 < i <= maxpage)]
    if pages[0] != 1:
        pages.insert(0, 1)
        if pages[1] != 2:
            pages.insert(1, '..')
    if pages[-1] != maxpage:
        pages.append(maxpage)
        if pages[-1] != maxpage - 1:
            pages.insert(-1, '..')
    return(pages)


def index(request, num=5, page=1):
    page -= 1
    books = Book.objects.all().order_by('-id')[page*num:(page+1)*num]
    pages = count_pages(num, page)
    context = {'num': num, 'page': pages, 'books': books}
    return render(request, 'books/index.html', context)


def detail(request, book_id):
    book = Book.objects.get(pk=book_id)
    context = {'book': book}
    return render(request, 'books/book_detail.html', context)


def genre_detail(request, genre_name):
    genre = get_object_or_404(Genre, name=genre_name)
    context = {'genre': genre}
    return render(request, 'books/genre_detail.html', context)


def genres(request):
    context = {'genres': Genre.objects.filter(base_genre=None)}
    return render(request, 'books/genres.html', context)


def about(request):
    return render(request, 'books/about.html')
