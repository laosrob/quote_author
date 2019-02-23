from __future__ import unicode_literals
from django.db import models
from apps.first_app.models import User

class UserManager(models.Manager):
    def message_check(self, postData):
        errors = {}
        if len(postData['message']) == 0:
            errors['message'] = "Quote cannot be blank"
        elif len(postData['message']) <10:
            errors['message'] = "Quote cannot be less than 10 characters"
        if len(postData['name']) == 0:
            errors['name'] = "Author cannot be blank"
        elif len(postData['message']) <3:
            errors['message'] = "Author name cannot be less than 3 characters"    
        return errors


class Message(models.Model):
    author = models.CharField(max_length=45)
    message = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messages")
    like = models.ManyToManyField(User, related_name="liked_messages")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager() 
