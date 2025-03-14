from django.contrib import admin
from unfold.admin import ModelAdmin
from libraryApi.books.models import Book, Author


@admin.register(Book)
class BookAdmin(ModelAdmin):
    pass

@admin.register(Author)
class AuthorAdmin(ModelAdmin):
    pass