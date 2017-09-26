# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from ..login.models import Member
import random, re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, related_name="books")
    reviewed_by = models.ManyToManyField(Member, related_name="reviewed_work")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ReviewManager(models.Manager):
    def create_review(self, formdata, memberid):
        if formdata['existing'] == "new" :
            author = Author.objects.create(name = formdata['author'])
        else :
            author = Author.objects.get(name = formdata['existing'])
        book = Book.objects.create(title = formdata['title'], author = author)

        review = self.create (
            content = formdata['content'],
            rating = formdata['rating'],
            member = Member.objects.get(id=memberid),
            book = book,
        )
        return review

    def add_review(self, formdata, memberid):
        author = Author.objects.get(name = formdata['existing'])
        book = Book.objects.get(title = formdata['title'])
        review = self.create (
            content = formdata['content'],
            rating = formdata['rating'],
            member = Member.objects.get(id=memberid),
            book = book,
        )
        return review

    def delete(self, reviewid):
        review = Review.objects.get(id = reviewid)
        review.delete()

class Review(models.Model):
    content = models.CharField(max_length=1000)
    rating = models.CharField(max_length=2)
    member = models.ForeignKey(Member, related_name="reviews")
    book = models.ForeignKey(Book, related_name="reviews")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ReviewManager()
