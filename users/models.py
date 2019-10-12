import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class CustomUser(AbstractUser):
    pass

    # add additional fields in here
    user_id = models.UUIDField('UUID', primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.email
