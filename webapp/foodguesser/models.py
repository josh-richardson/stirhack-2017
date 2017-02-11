from django.db import models

class ChatRoom(models.Model):
    topic = models.CharField(max_length=200)


    def __str__(self):
        return this.topic
