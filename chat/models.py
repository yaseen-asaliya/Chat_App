from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=100)

class Message(models.Model):
    text = models.TextField(max_length=100)

