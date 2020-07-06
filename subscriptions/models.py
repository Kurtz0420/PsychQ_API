import uuid

from creditcards.models import CardNumberField, CardExpiryField, SecurityCodeField
from django.db import models

# Create your models here.

from products.models import Product

PURCHASE_STATUS = (
    ('UNSPECIFIED_STATE', 0),
    ('PENDING', 2),
    ('PURCHASED', 1)
)


class Subscription(models.Model):
    id = models.UUIDField('UUID', primary_key=True, default=uuid.uuid4, editable=False)
    user_email = models.EmailField(max_length=100, null=False, blank=False, help_text="Email of the Subscriber")
    order_id = models.CharField(max_length=200, null=False, blank=False, help_text="Order Id From the Purchase")
    purchase_token = models.CharField(max_length=200, null=False, blank=False, help_text="Token From The Purchase")
    sku_product = models.CharField(max_length=100, null=False, blank=False, help_text="Product Which was subscribed to")
    package_name = models.CharField(max_length=100, null=False, blank=False, help_text="App For Which The Purchase Was Made")
    developer_payload = models.CharField(max_length=500, null=True, blank=True, help_text="Developer payload From The Purchase")
    original_json = models.CharField(max_length=1000, null=True, blank=True, help_text="Original Json from purchase")
    purchase_status = models.CharField(max_length=40, choices=PURCHASE_STATUS, default='UNSPECIFIED_STATE', help_text=" 0:Unspecified  1:Purchased  2:Pending ")
    purchase_time = models.CharField(max_length=200, null=True, blank=False, help_text="Time Of Purchase")
    is_acknowledged = models.BooleanField(default=False, help_text="Is the Purchase Acknowledged?")
    is_auto_renewing = models.BooleanField(default=False, help_text="Is the Subscription AutoRenewing?")
    purchase_signature = models.CharField(max_length=1000, null=False, blank=True, help_text="Purchase Signature")
    is_active = models.BooleanField(default=False, help_text="Is the Subscription Active or canceled?")

    def __str__(self):
        return str(self.user_email + ", " + str(self.purchase_token) + "" + self.purchase_time)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean_uuid(self):
        return self.id.__str__().replace('-', '')  # will clean up the uuid of dashes -
