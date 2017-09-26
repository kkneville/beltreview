from __future__ import unicode_literals
from django.db import models
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from models import *
import random, re
import bcrypt


def index(request):
    if "errors" not in request.session:
        request.session['errors'] = []
    context = {
        "errors": request.session['errors'],
    }
    request.session.pop("errors")
    return render(request, "login/index.html", context)

def addmember(request):
    if request.method == "POST":
        errors = Member.objects.validate_reg(request.POST)
        if errors:
            request.session['errors'] = errors
            return redirect("/index")
        member = Member.objects.create_member(request.POST)
        request.session['id'] = member.id
        return redirect(reverse("dashboard"))

def login(request):
    if request.method == "POST":
        result = Member.objects.validate_login(request.POST)
        if len(result['errors']) > 0 :
            request.session['errors'] = result['errors']
            return redirect("/index")
        else :
            member = result['member']
            request.session['id'] = member.id
        return redirect(reverse("dashboard"))

def logout(request):
    if "id" in request.session:
        request.session.pop('id')
    return redirect('/index')
