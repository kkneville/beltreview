# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string
from models import *
from django.db import models


def current_member(request):
    id = request.session['id']
    return Member.objects.get(id=id)

def logout(request):
    request.session.pop('id')
    request.session.pop('count')
    return redirect(reverse('/'))

def dashboard(request):
    member = current_member(request)
    reviews = Review.objects.all().order_by("-created_at")[:3]
    books = Book.objects.all().order_by("-created_at")
    context = {
        "member": member,
        "reviews": reviews,
        "books": books,
    }
    return render(request, "review/dashboard.html", context)

def addreview(request):
    member = current_member(request)
    existing = Author.objects.all()
    context = {
        "member": member,
        "existing": existing,
        "memberid": member.id,
    }
    return render(request, "review/addreview.html", context)

def add(request):
    review = Review.objects.create_review(request.POST, request.session['id'])
    if "count" not in request.session:
        request.session['count'] = 1
    else :
        request.session['count'] += 1
    return redirect(reverse('showbook', kwargs = {'id':review.book.id}))

def bookreview(request):
    bookreview = Review.objects.add_review(request.POST, request.session['id'])
    if "count" not in request.session:
        request.session['count'] = 1
    else :
        request.session['count'] += 1
    return redirect(reverse('showbook', kwargs = {'id':bookreview.book.id}))

def showbook(request, id):
    book = Book.objects.get(id=id)
    author = Author.objects.get(books=book)
    member = current_member(request)
    reviews = book.reviews.all()
    context = {
        "book": book,
        "member": member,
        "reviews": reviews,
        "author": author,
    }
    return render(request, "review/showbook.html", context)

def showmember(request, id):
    member = current_member(request)
    reviews = Review.objects.filter(member__id=member.id)
    count = request.session['count']
    context = {
        "member": member,
        "reviews": reviews,
        "count": count,
    }
    return render(request, "review/showmember.html", context)


def deletereview(request, id):
    Review.objects.delete(id)
    return redirect('/dashboard')
