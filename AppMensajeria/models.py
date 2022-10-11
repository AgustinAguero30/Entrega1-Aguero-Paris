from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from django.forms import IntegerField

# class Chat(models.Model):
#     emisor= models.ForeignKey(User, related_query_name="emisor_id", on_delete= models.CASCADE)
#     receptor= models.ForeignKey(User, related_name="receptor_id", on_delete= models.CASCADE)

# class Message(models.Model):
#     id_chat=models.ForeignKey(Chat, on_delete= models.CASCADE )  
#     emisor=models.ForeignKey(User, related_query_name="emisor_id", on_delete= models.CASCADE)
#     content= models.CharField(max_length=1000)
#     fecha= models.DateField(null=True)
#     is_read = models.BooleanField(default=False)