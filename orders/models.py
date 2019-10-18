import uuid

from creditcards.models import CardNumberField, CardExpiryField, SecurityCodeField
from django.db import models

# Create your models here.

from products.models import Product

ORDER_STATUS = (
    ('pending', 'PENDING'),
    ('shipped', 'SHIPPED'),
    ('completed', 'COMPLETED')
)


class Order(models.Model):
    order_id = models.UUIDField('UUID', primary_key=True, default=uuid.uuid4, editable=False)
    product_id = models.CharField(max_length=50, null=False, blank=False, help_text="Product which user ordered")
    user_id = models.CharField(max_length=50, null=False, blank=False, help_text="Id of the user who placed the order")
    country = models.CharField(max_length=30)
    # phone_number_with_code = PhoneField(blank=True, help_text='Contact phone number')
    phone_number_with_code = models.CharField(max_length=20)
    full_address = models.CharField("address", max_length=128)
    state = models.CharField(max_length=20)
    zip_code = models.CharField("zip code", max_length=5, default="43701")
    cc_number = CardNumberField('card number')
    cc_expiry = CardExpiryField('expiration date', null=True)
    cc_code = SecurityCodeField('security code')
    order_status = models.CharField(max_length=20, choices=ORDER_STATUS, default='pending')
    timestamp = models.DateTimeField(auto_now_add=True)

    # pic1 = models.CharField(max_length=300)
    # pic2 = models.CharField(max_length=300)
    # pic3 = models.CharField(max_length=300)

    def __str__(self):
        return str(self.product_id + ", " + str(self.order_id) + "" + self.user_id)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean_uuid(self):
        return self.order_id.__str__().replace('-', '')  # will clean up the uuid of dashes -
