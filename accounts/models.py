from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,UserManager

# Create your models here.

class UserAccountManager(UserManager):
    def create_user(self, email ,  name ,password=None):
        email = self.normalize_email(email)
        if not email:
            raise ValueError("user must have an email")
        user = self.model(email=email,name=name)
        user.set_password(password)
        user.save()

        return user

class UserAccount(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length=255, unique= True)
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()
    USERNAME_FIELD =  "email"
    REQUIRED_FIELDS = ["name"]

    def __str__(self) -> str:
        return self.name

    def get_full_name(self):
        return self.name 
    def get_short_name(self):
        return self.name   