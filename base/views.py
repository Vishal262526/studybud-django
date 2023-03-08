from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(req):
    return render(req, 'base/home.html')

def rooms(req):
    rooms = [
        {'id':"1",'name':"Lets Learn Python"},
        {'id':"2",'name':"Lets Learn JS"},
        {'id':"3",'name':"Lets Learn C++"},
    ]

    return render(req, 'base/rooms.html',{"data":rooms})
