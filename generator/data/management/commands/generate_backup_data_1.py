from io import StringIO
import pandas as pd
from contextlib import closing
from data.models import DatasetGenerate, DatasetBackup1
from django.db import models
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        result = self.backup()
        self.insert_dataset_generate(result)

    def backup(self):
        #table_name = Dataset.objects.model._meta.db_table
        #raw_query = f'select sum(count) AS count, dest_wallet_id, transaction_type, wallet_nickname, sum(transaction_cost) AS transaction_cost, sum(transaction_value) AS transaction_value from {table_name} group by dest_wallet_id, transaction_type, wallet_nickname'
        results = DatasetGenerate.objects.values(
            'dest_wallet_id',
            'transaction_type',
            'wallet_nickname'
        ).annotate(
            count=models.Sum('count'),
            transaction_cost=models.Sum('transaction_cost'),
            transaction_value=models.Sum('transaction_value')
        )

        return results

    def insert_dataset_generate(self, data):
        mem_csv = self.in_memory_csv(data)
        with closing(mem_csv) as csv_io:
            insert_count = DatasetBackup1.objects.from_csv(csv_io)
            print(f"{insert_count} records inserted")

    def in_memory_csv(self, data):
        mem_csv = StringIO()
        pd.DataFrame(data).to_csv(mem_csv, index=False)
        mem_csv.seek(0)
        return mem_csv