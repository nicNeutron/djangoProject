from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

def home(request):
    return HttpResponse('Hello world ! This is Home!')

def faq(request):
    return HttpResponse('Hello world ! This is FAQ')

def display_date(request):
    date_joined = datetime.today().year
    return HttpResponse(date_joined)

def message(request):
    text = """<h1 style="color: #F4CE14;"> This is a message in HTML! </h1>"""
    return HttpResponse(text)