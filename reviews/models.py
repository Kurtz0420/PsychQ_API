import uuid as uuid
from django.db import models

# Create your models here.

from products.models import Product


class Review(models.Model):
    id = models.UUIDField('UUID', primary_key=True, default=uuid.uuid4, editable=False)
    product_id = models.CharField(max_length=60, null=False, blank=False, help_text="Product id on which review is made")
    user_id = models.CharField(max_length=50, null=False, blank=False, help_text="id of the user who made the review")
    title = models.CharField(max_length=100, help_text="Title of the review")
    description = models.CharField(max_length=1000, help_text="Body of the review")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(str(self.id) + "" + self.product_id + ", " + self.user_id + "" + self.title)

    def __init__(self, *args, **kwargs):
        super(Review, self).__init__(*args, **kwargs)

    # def clean_id(self):
    #     return self.id.__str__().replace('-', '')  # will clean up the uuid of dashes -
