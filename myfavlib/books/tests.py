from django.test import TestCase
from .models import Book, Author, Genre, UNKNOWN


class GenreTestCase(TestCase):
    def test_genre_created_properly(self):
        """
        Жанры создаются
        """
        genre = Genre.objects.create(name=Genre.FICTION)
        self.assertEqual(genre.name, Genre.FICTION)
        self.assertEqual(genre.base_genre, None)

    def test_genre_inherited_properly(self):
        """
        Жанры наследуются
        """
        par = Genre.objects.create(name=Genre.FICTION)
        Genre.objects.create(name=Genre.FANTAZY, base_genre=par)
        self.assertEqual(par.children.count(), 1)
        par.children.create(name=Genre.SCIFI)
        self.assertEqual(par.children.count(), 2)
        self.assertEqual(str(par.children.all()), '<QuerySet [<Genre: FTZ>, <Genre: SCI>]>')
        self.assertEqual(str(Genre.objects.get(name=Genre.SCIFI).base_genre), Genre.FICTION)


class AuthorTestCase(TestCase):
    def test_author_created_properly(self):
        """
        Авторы создаются
        """
        Author.objects.create(name='Shakespeare', country='UK')
        test_auth = Author.objects.get(id=1)
        self.assertEqual(test_auth.name, 'Shakespeare')

    def test_unknown_values_work(self):
        """
        Создание автора с неизвестными параметрами
        """
        auth = Author.objects.create()
        self.assertEqual(auth.name, UNKNOWN)
        self.assertEqual(auth.country, UNKNOWN)


class BookTestCase(TestCase):

    def test_book_links_properly(self):
        b = Book.objects.create(name='Sienza')
        a1 = Author.objects.create(name='Wolf Wolffson', country='SE')
        a1.book_set.add(b)
        self.assertEqual(b.author.all()[0].name, 'Wolf Wolffson')
        a2 = Author.objects.create(name='Nil Nilson', country='SE')
        b.author.add(a2)
        self.assertEqual(b.author.all()[1].name, 'Nil Nilson')

    def test_book_gets_genre_properly(self):
        b = Book.objects.create(name='Sienza')
        b.genre.create(name=Genre.SCIFI)
        genres = b.genre.all()
        self.assertEqual(genres[0].name, Genre.SCIFI)

    def test_filter_genre(self):
        b1 = Book.objects.create(name='Sienza')
        g = Genre.objects.create(name=Genre.SCIFI)
        b1.genre.add(g)
        b2 = Book.objects.create(name='Lol')
        b2.genre.add(g)
        self.assertEqual(Book.objects.filter(genre__name=Genre.SCIFI).count(), 2)
