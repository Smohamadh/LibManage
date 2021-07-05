from django.contrib import admin
from LMapp.models import Author, Publisher, Book


class AuthorModelAdmin(admin.ModelAdmin):
    list_filter = ['books']

    class Meta:
        model = Author


class BookModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'number_of_pages', 'year_of_publication']
    list_filter = ['authors', 'publisher']
    search_fields = ['title']

    class Meta:
        model = Book


admin.site.register(Author, AuthorModelAdmin)
admin.site.register(Publisher)
admin.site.register(Book, BookModelAdmin)
