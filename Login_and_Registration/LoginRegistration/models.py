from django.db import models
import re

class userManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['firstname']) < 2:
            errors["firstname"] = "first name should be at least 2 characters"


        if len(postData['lastname']) < 2:
            errors["lastname"] = "last name should be at least 2 characters"

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"


        if len(postData['password']) < 8:
            errors["desc"] = "password should be at least 8 characters"

        if postData['password']!=postData['cpassword']:
            errors["password"] = "Password and its confirmation does not match"   

        


        return errors

class user(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = userManager()

