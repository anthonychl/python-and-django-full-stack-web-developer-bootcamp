from django.db import models
from django.contrib import auth

# Create your models here.
class User(auth.models.User, auth.models.PermissionsMixin):
    
    def __str__(self):
        return f"@{self.username}" # return "@{}".format(self.username) it was like this originally. We use '@' to give it a twitter handle feel to it. username is an inherited attribute

