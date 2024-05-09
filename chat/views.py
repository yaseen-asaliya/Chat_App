from django.shortcuts import render
from chat.models import Room, Message

# Create your views here.
def index(request):
    rooms = Room.objects.all()
    return render(request, "chat/index.html", {"rooms": rooms})


def room(request, room_name):
    room = Room.objects.create(name=room_name)
    
    return render(request, 'chat/room.html')

    
