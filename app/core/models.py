from django.db import models
from django.contrib.auth.models import AbstractUser , BaseUserManager , PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self , email ,username , password=None , **extra_fields ):

        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')
        user = self.model(email=self.normalize_email(email),
		username=username , **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):

        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractUser , PermissionsMixin):
    email = models.EmailField(max_length=255 , unique=True)
    phone = models.CharField(max_length=20)
    username = models.CharField(max_length=20, primary_key=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']