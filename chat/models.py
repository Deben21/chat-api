from django.db import models
from useraccount.models  import User
from useraccount.models import User

class ChatRoom(models.Model):
    participants = models.ManyToManyField(User)
    

    def __str__(self):
        return f"ChatRoom {self.id}"
    
class Message(models.Model):
    room = models.ForeignKey(ChatRoom, related_name='messages', on_delete=models.CASCADE)
    sender = models.ForeignKey(User,on_delete=models.CASCADE)
    # recipient = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.sender.name}: {self.content[:20]}"
    