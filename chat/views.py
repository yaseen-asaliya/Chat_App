from django.shortcuts import render, get_object_or_404
from chat.models import Room, Message

def index(request):
    rooms = Room.objects.all()
    return render(request, "chat/index.html", {"rooms": rooms})


def room(request, room_name):

    return render(request, 'chat/room.html')

    

