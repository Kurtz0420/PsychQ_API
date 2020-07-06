import uuid

from django.conf import settings
from django.db import models
from django.db.models import IntegerField
from django.urls import reverse

from rest_framework.reverse import reverse as api_reverse


# Create your models here.

class UserJoke(models.Model):
    id = models.UUIDField('UUID', primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=120, help_text="Username of the user")
    email = models.CharField(max_length=100, help_text="Email Of The User")
    build_up = models.CharField(max_length=1300, null=True, help_text="Build up or first line of the joke")
    delivery = models.CharField(max_length=300, null=True, blank=True,
                                help_text="2nd Part of joke : if joke is only one liner then leave this one empty")
    type = models.CharField(max_length=120, null=True, blank=True,
                            help_text="Type of joke : User will choose from pre-defined choices")
    slug = models.CharField(max_length=120, help_text="Gif/Thumb/other Url - If Any", blank=True, null=True)
    thumbs_ups = models.IntegerField(default=0)
    thumbs_downs = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(str(self.id) + ", " + self.username)

    def __init__(self, *args, **kwargs):
        super(UserJoke, self).__init__(*args, **kwargs)

        # @property

    # def owner(self):
    #    return self.user
    #
    # # def get_absolute_url(self):
    # #     return reverse("api-postings:post-rud", kwargs={'pk': self.pk}) '/api/postings/1/'
    #
    # def get_api_url(self, request=None):
    #    return api_reverse("api-postings:post-rud", kwargs={'pk': self.pk}, request=request)
    def clean_uuid(self):
        return self.id.__str__().replace('-', '')  # will clean up the uuid of dashes -
