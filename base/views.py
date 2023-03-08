from django.shortcuts import render
from django.http import HttpResponse
from .models import Room
# Create your views here.




def index(req):
    return render(req, 'base/home.html')

def rooms(req):
    room = Room.objects.all()
    print(room)
    # return
    return render(req, 'base/rooms.html',{"data":room})


def room(req, id):
    room = Room.objects.get(id = id)
    print(".........................")
    print(room)
    return render(req, 'base/single-room.html', {"data":room})
