import os

import boto3

table = boto3.resource(
    "dynamodb"
).Table(
    os.environ["TABLE_NAME"]
)


class TransactionRepository:

    @staticmethod
    def save(transaction):

        table.put_item(
            Item=transaction
        )