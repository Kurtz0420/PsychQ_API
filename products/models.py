from django.db import models


class Product(models.Model):
    id = models.CharField(max_length=100, null=False, blank=False, unique=True, primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    quantity_in_stock = models.IntegerField()
    sales = models.IntegerField()
    price = models.IntegerField()
    shipment_charges = models.IntegerField()
    photos = models.CharField(max_length=2000)

    # we can format reviews as uuid and a string of review
    # reviews = models.ForeignKey(Reviews, to_field='title', db_column='reviews', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id + ", " + self.name)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # @property
    # def owner(self):
    #    return self.user
    #
    # # def get_absolute_url(self):
    # #     return reverse("api-postings:post-rud", kwargs={'pk': self.pk}) '/api/postings/1/'
    #
    # def get_api_url(self, request=None):
    #    return api_reverse("api-postings:post-rud", kwargs={'pk': self.pk}, request=request)

# class Reviews(models.Model):
#     user_id = models.ForeignKey(Account.uuid, on_delete=models.CASCADE)
#     title = models.CharField(max_length=300)
#     description = models.CharField(max_length=2000)
#
#     def __str__(self):
#         return str(self.user_id + ", " + self.title + ", " + self.description)
#
#     class Meta:
#         ordering = ('headline',)
# def __init__(self, *args, **kwargs):
#     super().__init__(*args, **kwargs)

# class Photos(models.Model)
