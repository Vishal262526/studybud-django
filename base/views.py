from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


rooms = [
        {'id':"1",'name':"Lets Learn Python"},
        {'id':"2",'name':"Lets Learn JS"},
        {'id':"3",'name':"Lets Learn C++"},
    ]

def index(req):
    return render(req, 'base/home.html')

def rooms(req):
    rooms = [
        {'id':"1",'name':"Lets Learn Python"},
        {'id':"2",'name':"Lets Learn JS"},
        {'id':"3",'name':"Lets Learn C++"},
    ]

    return render(req, 'base/rooms.html',{"data":rooms})


def room(req, id):
    context = {"data":{}}
    for data in room:
        if data['id'] == id:
            context['data'] = data
            break
    return render(req, 'base.single-room.html', context)
