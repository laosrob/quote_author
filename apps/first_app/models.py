from __future__ import unicode_literals
from django.db import models

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {} # add keys and values to errors dictionary for each invalid field
        email_match = User.objects.filter(email_address=postData['email'])
        if len(postData['first_name']) == 0:
            errors['first_name'] = "First Name cannot be blank"
        elif len(postData['first_name']) < 2:
            errors["first_name"] = "First Name should be at least 2 characters"
        elif postData['first_name'].isalpha() == False:
            errors['first_name'] = "First Name must contian only letters"
        if len(postData['last_name']) == 0:
            errors['last_name'] = "Last Name cannot be blank"
        elif len(postData['last_name']) < 3:
            errors["last_name"] = "Last Name should be at least 3 characters"
        elif postData['last_name'].isalpha() == False:
            errors['last_name'] = "Last Name must contian only letters"
        if len(postData['email']) == 0:
            errors['email'] = "Email cannot be blank"
        elif len(email_match) > 0:
            errors['email'] = 'That email exists in the database already'
        if postData['password'] != postData['confirmpw']:
            errors["confirmpw"] = "Password must match"
        if len(postData['password']) < 8:
            errors["password"] = "Password should be at least 8 characers"
        print(errors)
        return errors
    def basic_login(self, postData):
        errors = {} # add keys and values to errors dictionary for each invalid field
        user = User.objects.filter(email_address=postData['email'])
        if len(postData['password']) == 0:
            errors['password'] = "Please enter password"
        if len(postData['email']) == 0:
            errors['email'] = "Please enter email"
        elif len(user) == 0:
            errors['email_address'] = "Invalid email"
        else:
            user = User.objects.get(email_address=postData['email'])
            if user.password != postData["password"]:
                errors['password'] = "Password does not match"
        print(errors)
        return errors

    def edit_validator(self, postData):
        errors = {} # add keys and values to errors dictionary for each invalid field
        email_match = User.objects.filter(email_address=postData['email'])
        if len(postData['first_name']) == 0:
            errors['first_name'] = "First Name cannot be blank"
        elif len(postData['first_name']) < 2:
            errors["first_name"] = "First Name should be at least 2 characters"
        elif postData['first_name'].isalpha() == False:
            errors['first_name'] = "First Name must contian only letters"
        if len(postData['last_name']) == 0:
            errors['last_name'] = "Last Name cannot be blank"
        elif len(postData['last_name']) < 3:
            errors["last_name"] = "Last Name should be at least 3 characters"
        elif postData['last_name'].isalpha() == False:
            errors['last_name'] = "Last Name must contian only letters"
        if len(postData['email']) == 0:
            errors['email_address'] = "Email cannot be blank"
        elif len(email_match) > 0:
            errors['email'] = 'That email exists in the database already'
        if postData['password'] != postData['confirmpw']:
            errors["confirmpw"] = "Password must match"
        if len(postData['password']) < 8:
            errors["password"] = "Password should be at least 8 characers"
        print(errors)
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email_address = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    confirm_password = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager() 

 