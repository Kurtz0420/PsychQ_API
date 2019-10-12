from django.conf import settings
from django.db import models
from django.db.models import IntegerField
from django.urls import reverse

from rest_framework.reverse import reverse as api_reverse


# Create your models here.

class Category(models.Model):

    id = models.CharField(max_length=100, null=False, blank=False, unique=True, primary_key=True)
    title = models.CharField(max_length=120, unique=True)
    description = models.CharField(max_length=1300, null=True, blank=True)
    sub_categories = models.CharField(max_length=120, null=True, blank=True)
    pic_top = models.CharField(max_length=300)
    pic_left = models.CharField(max_length=300)
    pic_right = models.CharField(max_length=300)
    count_range_from = models.IntegerField()
    count_range_to = models.IntegerField()
    tags = models.CharField(max_length=500)
    total_posts_count = models.IntegerField()

    def __str__(self):
        return str(self.id + ", " + self.title)

    def __init__(self, *args, **kwargs):
        super(Category, self).__init__(*args, **kwargs)

        # @property
    # def owner(self):
    #    return self.user
    #
    # # def get_absolute_url(self):
    # #     return reverse("api-postings:post-rud", kwargs={'pk': self.pk}) '/api/postings/1/'
    #
    # def get_api_url(self, request=None):
    #    return api_reverse("api-postings:post-rud", kwargs={'pk': self.pk}, request=request)
