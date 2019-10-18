from django.conf import settings
from django.db import models
from django.db.models import IntegerField
from django.urls import reverse

from rest_framework.reverse import reverse as api_reverse


# Create your models here.

class Category(models.Model):

    id = models.CharField(max_length=100, null=False, blank=False, unique=True, primary_key=True, help_text="Unique Id")
    title = models.CharField(max_length=120, unique=True, help_text="Name of the category")
    description = models.CharField(max_length=1300, null=True, blank=True, help_text="Brief Description")
    sub_categories = models.CharField(max_length=120, null=True, blank=True, help_text="If any")
    pic_top = models.CharField(max_length=300)
    pic_left = models.CharField(max_length=300)
    pic_right = models.CharField(max_length=300)
    count_range_from = models.IntegerField(help_text="Universal Count where this category starts")
    count_range_to = models.IntegerField(help_text="Universal Count where this category ends")
    tags = models.CharField(max_length=500, help_text="Tags for modified searching")
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
