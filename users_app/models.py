from django.db import models
from encrypted_model_fields.fields import EncryptedCharField
# Create your models here.
class UserOrder(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = EncryptedCharField(max_length=100)
    phone_number = EncryptedCharField(max_length=100, null="true")
    country = models.CharField(max_length=100)
    city = EncryptedCharField(max_length=100)
    zipcode = EncryptedCharField(max_length=100)
    address1 = EncryptedCharField(max_length=100)
    address2 = EncryptedCharField(max_length=100)
    order_date = models.DateField()
