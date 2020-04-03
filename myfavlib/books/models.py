import math

from django.db import models
from django.utils import timezone

UNKNOWN = 'unknown'


class Author(models.Model):
    name = models.CharField(max_length=50, default=UNKNOWN)
    country = models.CharField(max_length=100, default=UNKNOWN, blank=True)

    def __str__(self):
        a = 1
        bin(a)
        return self.name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Genre(models.Model):
    DETECTIVE = 'DT'
    FICTION = 'FN'
    FANTAZY = 'FTZ'
    SCIFI = 'SCI'
    SOCFI = 'SOF'
    GENRES = (
        (DETECTIVE, 'Детектив'),
        (FICTION, 'Фантастика'),
        (FANTAZY, 'Фэнтези'),
        (SCIFI, 'Научная фантастика'),
        (SOCFI, 'Социальная фантастика'),
    )
    name = models.CharField(max_length=3, unique=True, choices=GENRES)
    base_genre = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='children')

    def get_children_all(self):
        pass

    def __str__(self):
        return self.get_name_display()

    def get_children(self):
        return Genre.objects.filter(base_genre=self)

    def get_books(self):
        return self.book_set.all()

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.ManyToManyField(Author, default=UNKNOWN, blank=True)
    genre = models.ManyToManyField(Genre, default=UNKNOWN, blank=True)
    cover = models.ImageField(upload_to='images', null=True, blank=True)
    text = models.FileField(upload_to='texts', null=True)
    annot = models.CharField(max_length=2000, null=True)
    post_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def get_annot(self):
        if self.annot is None:
            return("Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
                   "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
                   "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris "
                   "nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit "
                   "in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat "
                   "non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
        else:
            return self.annot

    def get_author(self):
        if self.author.count() == 0 or self.author.all()[0].name == UNKNOWN:
            return('Неизвестный')
        else:
            names = ", ".join([str(i) for i in self.author.all()])
            return(names)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
