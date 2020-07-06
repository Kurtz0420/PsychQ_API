from django.conf import settings
from django.db import models
from django.db.models import IntegerField
from django.urls import reverse

from rest_framework.reverse import reverse as api_reverse


# Create your models here.

class Joke(models.Model):
    id = models.CharField(max_length=100, null=False, blank=False, unique=True, primary_key=True)
    custom_ordering = models.IntegerField(default=0)
    about = models.CharField(max_length=120, help_text="What the joke is about : ex : Two Jews, Blacks, White")
    build_up = models.CharField(max_length=1300, null=True, help_text="Build up or first line of the joke")
    delivery = models.CharField(max_length=120, null=True, blank=True, help_text="2nd Part of joke : if joke is only one liner then leave this one empty")
    type = models.CharField(max_length=120, null=True, blank=True, help_text="Type of joke : category")
    thumb_slug = models.CharField(max_length=120, help_text="Thumbnail Url - if any", null=True, blank=True)
    full_slug = models.CharField(max_length=120, help_text="Full Resolution Url of Thumb - If Any", null=True, blank=True)
    gif_slug = models.CharField(max_length=120, help_text="Gif Url - If Any", null=True, blank=True)
    nsfw = models.BooleanField(default=False, help_text="True : when joke not safe for work (for example sexually explicit jokes)")
    religious = models.BooleanField(default=False, help_text="True : when joke against certain religions and their prejudices")
    political = models.BooleanField(default=False, help_text="True : when joke against politics / politicians ")
    thumbs_ups = models.IntegerField(default=0)
    thumbs_downs = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id + ", " + self.about)

    def __init__(self, *args, **kwargs):
        super(Joke, self).__init__(*args, **kwargs)

        # @property
    # def owner(self):
    #    return self.user
    #
    # # def get_absolute_url(self):
    # #     return reverse("api-postings:post-rud", kwargs={'pk': self.pk}) '/api/postings/1/'
    #
    # def get_api_url(self, request=None):
    #    return api_reverse("api-postings:post-rud", kwargs={'pk': self.pk}, request=request)
