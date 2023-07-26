from django.contrib import admin
from django.db import models
# Register your models here.

from .models import Dataset


class DatasetAdmin(admin.ModelAdmin):
    list_display = ['time_internal', 'count', 'dest_wallet_id', 'transaction_type', 'transaction_type_chain', 'wallet_nickname', 'transaction_cost', 'transaction_value', 'bank_id', 'transaction_gateway_id']

admin.site.register(Dataset, DatasetAdmin)