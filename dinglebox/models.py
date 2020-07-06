from django.conf import settings
from django.db import models
from django.db.models import IntegerField
from django.urls import reverse

from rest_framework.reverse import reverse as api_reverse


# Create your models here.

class Clip(models.Model):
    id = models.CharField(max_length=100, null=False, blank=False, unique=True, primary_key=True)
    custom_ordering = models.IntegerField(default=0)
    title = models.CharField(max_length=120, unique=True, help_text="Name of the Track")
    description = models.CharField(max_length=1300, null=True, blank=True, help_text="Brief description (if any)")
    audio_link = models.CharField(max_length=1300, null=False, blank=False, help_text="link of the track")
    thumb_small = models.CharField(max_length=1300, null=True, blank=True, help_text="Link of small image")
    thumb_large = models.CharField(max_length=1300, null=True, blank=True, help_text="Link of a bit large image")
    have_ad = models.BooleanField(default=False, help_text="Will it contain ad")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id + ", " + self.title)

    def __init__(self, *args, **kwargs):
        super(Clip, self).__init__(*args, **kwargs)

        # @property
    # def owner(self):
    #    return self.user
    #
    # # def get_absolute_url(self):
    # #     return reverse("api-postings:post-rud", kwargs={'pk': self.pk}) '/api/postings/1/'
    #
    # def get_api_url(self, request=None):
    #    return api_reverse("api-postings:post-rud", kwargs={'pk': self.pk}, request=request)
