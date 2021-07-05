from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    family = models.CharField(max_length=150)
    alias = models.CharField(max_length=100)
    books = models.ManyToManyField('Book')

    def __str__(self):
        return self.name + ' ' + self.family


class Publisher(models.Model):
    name = models.CharField(max_length=150)
    tel = models.CharField(max_length=12)
    address = models.TextField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=150)
    number_of_pages = models.IntegerField()
    year_of_publication = models.DateField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.title
