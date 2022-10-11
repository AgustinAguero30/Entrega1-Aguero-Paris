from django import forms
from django.contrib.auth.models import User

# class Message(forms.Form):
#     id_chat=models.ForeignKey(Chat, on_delete= models.CASCADE )  
#     emisor=models.ForeignKey(User, related_query_name="emisor_id", on_delete= models.CASCADE)
#     content= models.CharField(max_length=1000)
#     fecha= models.DateField(null=True)
#     is_read = models.BooleanField(default=False)