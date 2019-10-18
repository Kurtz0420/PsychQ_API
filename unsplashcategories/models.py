from django.conf import settings
from django.db import models
from django.db.models import IntegerField
from django.urls import reverse

from rest_framework.reverse import reverse as api_reverse


# Create your models here.

class UnsplashCategory(models.Model):

    id = models.CharField(max_length=100, null=False, blank=False, unique=True, primary_key=True)
    title = models.CharField(max_length=120, unique=True, help_text="Name of the category")
    description = models.CharField(max_length=1300, null=True, blank=True, help_text="Brief description of category")
    pic_top = models.CharField(max_length=300)
    pic_left = models.CharField(max_length=300)
    pic_right = models.CharField(max_length=300)
    related_tags = models.CharField(max_length=500, help_text="Related searches that appear after search")
    total_posts_count = models.IntegerField()

    def __str__(self):
        return str(self.id + ", " + self.title)

    def __init__(self, *args, **kwargs):
        super(UnsplashCategory, self).__init__(*args, **kwargs)

        # @property
    # def owner(self):
    #    return self.user
    #
    # # def get_absolute_url(self):
    # #     return reverse("api-postings:post-rud", kwargs={'pk': self.pk}) '/api/postings/1/'
    #
    # def get_api_url(self, request=None):
    #    return api_reverse("api-postings:post-rud", kwargs={'pk': self.pk}, request=request)
