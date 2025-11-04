from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS = ((0, "Availble"), (1, "On Loan"))


class Category(models.Model):
    category_code = models.CharField(max_length=10, unique=True)
    category_description = models.CharField(max_length=100, unique=False)

    def __str__(self):
        return self.category_code + ", " + self.category_description
    

class Book(models.Model):
    book_code = models.CharField(max_length=10, unique=True)
    title = models.CharField(max_length=50, unique=False)
    author = models.CharField(max_length=50, unique=False)
    book_category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="books_in_this_category")
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.title + ", " + self.author


class Borrower(models.Model):
    borrower_code = models.CharField(max_length=10, unique=True)
    given_name = models.CharField(max_length=25, unique=False)
    family_name = models.CharField(max_length=20, unique=False)
    books_out = models.IntegerField(default=0)

    def __str__(self):
        return self.borrower_code + ", " + self.given_name + ", " + self.family_name
    

class Loan(models.Model):
    loan_number = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="book_borrowed")
    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE, related_name="person_borrowing")
    borrowed_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.loan_number) + ", " + self.borrower.family_name + ", " + self.book.title + ", " + self.borrowed_on.isoformat()
    