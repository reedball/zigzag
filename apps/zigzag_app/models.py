from __future__ import unicode_literals
from django.db import models
import re


# # Create your models here.

class UserManager(models.Manager):
    def validator(self,postData):
        print('*' * 100)
        print('postData: ',postData)
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = ("Invalid email address!")
        # add keys and values to errors dictionary for each invalid field
        if len(postData['first_name']) < 2:
            errors["first_name"] = "Your first name is too short"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Your last name is too short"
        if len(postData['password']) < 8:
            errors["password"] = "Your password is too short"
        if postData['confirm_pw'] != postData['password']:
            errors['confirm_pw'] = "Your passwords do not match"
        return errors

class JobManager(models.Manager):
    def jobvalidator(self,postData):
        print('Wishvalidator is working')
        errors = {}
        if len(postData['title']) < 3:
            errors['title'] = "A job must consist of at least 3 characters!"
        if len(postData['location']) < 1:
            errors['location'] = "A location must be provided"
        return errors

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, default=None)
    location = models.CharField(max_length=255)
    category = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name="jobs_uploaded")
    picked_by = models.ManyToManyField(User, related_name="jobs_picked")
    is_chosen = models.BooleanField(default=False)
    objects = JobManager()

