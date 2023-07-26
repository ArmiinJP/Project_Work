from django.db import models
from postgres_copy import CopyManager
from django.utils import timezone


class Dataset(models.Model):
    time_internal = models.DateTimeField(primary_key=True)
    count = models.IntegerField()
    dest_wallet_id = models.BigIntegerField()
    transaction_type = models.IntegerField()
    #transaction_type_chain = ArrayField(models.CharField(max_length=128), blank=True)
    transaction_type_chain = models.CharField(max_length=128)
    wallet_nickname = models.CharField(max_length=16, null=True, blank=True)
    transaction_cost = models.BigIntegerField()
    transaction_value = models.BigIntegerField()
    bank_id = models.IntegerField()
    transaction_gateway_id = models.CharField(max_length=8)

    objects = CopyManager()