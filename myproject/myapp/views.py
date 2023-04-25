from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

def home(request):
    path = request.path # access path property inside request object
    scheme = request.scheme
    method = request.method
    address = request.META['REMOTE_ADDR']
    user_agent = request.META['HTTP_USER_AGENT']
    path_info = request.path_info

    response = HttpResponse("This Works !")
    response.headers['Age'] = 20

    msg = f""" <br>
        <br>Path: {path}
        <br>Address: {address}
        <br>Scheme: {scheme}
        <br>Method: {method}
        <br>User agent: {user_agent}
        <br>Path info: {path_info}
        <br>
        <br> Response header: {response.headers}
            
    """

    #return HttpResponse('Hello world ! This is Home!')
    return HttpResponse(msg, content_type='text/html', charset='utf-8')

def faq(request):
    return HttpResponse('Hello world ! This is FAQ')

def display_date(request):
    date_joined = datetime.today().year
    return HttpResponse(date_joined)

def message(request):
    text = """<h1 style="color: #F4CE14;"> This is a message in HTML! </h1>"""
    return HttpResponse(text)

def menuitems(request, dish):
    items = {
        'pasta': 'Pasta is a type of noodle',
        'falafel': 'Falafel are deep fried mashed chickpeas',
        'cheesecake': 'Cheesecake is a creamy dessert'
    }
    description = items[dish]

    return HttpResponse(f"<h2> {dish} </h2>" + description)