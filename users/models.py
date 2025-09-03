from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, username,phone=None, password=None,**extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email,
                          username=username,
                          phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, phone, password,**extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, username, phone, password, **extra_fields)

class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=16, unique=True, blank=False, null=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone']

    def __str__(self):
        return self.username
