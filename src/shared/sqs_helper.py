import os
import json
import boto3

from shared.logger import logger

sqs = boto3.client("sqs")


class SQSHelper:

    @staticmethod
    def send_message(transaction: dict):

        response = sqs.send_message(
            QueueUrl=os.environ["QUEUE_URL"],
            MessageBody=json.dumps(transaction),
            MessageGroupId="bank-transactions"
        )

        logger.info(
            f"Message sent successfully. MessageId={response['MessageId']}"
        )

        return response