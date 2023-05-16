
# from datetime import datetime

# Create your models here.
# class Room(models.Model):
#     name = models.CharField(max_length=1000)
# class Message(models.Model):
#     value = models.CharField(max_length=1000000)
#     date = models.DateTimeField(default=datetime.now, blank=True)
#     user = models.CharField(max_length=1000000)
#     room = models.CharField(max_length=1000000)




# Create your models here.
# from django.db import models
# from django.contrib.auth.models import User

# from .models import tbl_login


# class Message(models.Model):
#     sender = models.ForeignKey(tbl_login, on_delete=models.CASCADE, related_name='sent_messages',blank=True,null=True)
#     recipient = models.ForeignKey(tbl_login, on_delete=models.CASCADE, related_name='received_messages',blank=True,null=True)
#     message = models.TextField(blank=True,null=True)
#     timestamp = models.DateTimeField(auto_now_add=True,blank=True,null=True)


from django.db import models
from Schoolapp.models import tbl_login, teacher_detail


class Message(models.Model):
    sender = models.ForeignKey(tbl_login, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(teacher_detail, on_delete=models.CASCADE, related_name='receiver')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender.email} to {self.receiver.email}"

