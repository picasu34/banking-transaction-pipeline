import boto3
import json
import os

events = boto3.client("events")

BUS_NAME = os.environ["EVENT_BUS_NAME"]


class EventBridgeHelper:

    @staticmethod
    def publish(transaction):

        response = events.put_events(
            Entries=[
                {
                    "Source": "bank.transaction",
                    "DetailType": "TransactionProcessed",
                    "Detail": json.dumps(transaction),
                    "EventBusName": BUS_NAME
                }
            ]
        )

        return response