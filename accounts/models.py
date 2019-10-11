import uuid

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class MyAccountManager(BaseUserManager):
    # REQUIRED FIELDS NEEDS TO BE ADDED HERE!!!
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

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


class Account(AbstractBaseUser):
    uuid = models.UUIDField('UUID', primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    # Above fields are required in making a custom user model in django, we can
    # add as many fields from here
    profile_pic = models.CharField(max_length=200)
    # here create order's count field that would be foreign key for product
    # order's count = Product.objects.filter(username=self.username).count() or something

    USERNAME_FIELD = 'email'  # this will be used for login
    REQUIRED_FIELDS = ['username']  # Required fields goes here

    objects = MyAccountManager()

    def __str__(self):  # Similar to a toString method in android
        return self.email + ", " + self.username  # Will print email when account object used

    # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True

    def set_uuid(self, uuid4):
        pass

    def clean_uuid(self):
        return self.uuid.__str__().replace('-', '')  # will clean up the uuid of dashes -

