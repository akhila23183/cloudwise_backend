from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)

class CustomUserManager(BaseUserManager):

    def create_user(self, email, username, password=None):

        if not email:
            raise ValueError("Email is required")

        user = self.model(
            email=self.normalize_email(email),
            username=username
        )

        user.set_password(password)
        user.save(using=self._db)

        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(unique=True)

    username = models.CharField(max_length=100)

    is_active = models.BooleanField(default=True)

    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
 
 
