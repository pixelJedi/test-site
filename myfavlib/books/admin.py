from django.contrib import admin

from .models import Book, Author, Genre


class GenreInline(admin.TabularInline):
    model = Genre
    extra = 1


class BookAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,      {'fields': ['name', 'author', 'annot', ('cover', 'text')]}),
        ('Тэги',    {'fields': ['genre']}),
        (None,      {'fields': ['post_date']})
    ]
#    inlines = [GenreInline]
    list_filter = ['genre']
    filter_vertical = ('genre', 'author')


admin.site.register(Book, BookAdmin)
admin.site.register(Genre)
admin.site.register(Author)


# Register your models here.
