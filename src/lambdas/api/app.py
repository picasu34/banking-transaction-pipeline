import json
import os
import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

sqs = boto3.client("sqs")

QUEUE_URL = os.environ["QUEUE_URL"]
REQUIRED_FIELDS = [
    "transaction_id",
    "customer_id",
    "customer_name",
    "account_number",
    "transaction_type",
    "amount",
    "currency",
    "merchant",
    "channel",
    "branch",
    "timestamp"
]


def lambda_handler(event, context):
    logger.info("API Lambda Started")

    logger.info("API Request Received")

    try:

        if "body" not in event:
            return {
                "statusCode": 400,
                "body": json.dumps({
                    "status": "FAILED",
                    "message": "Request body is missing."
                })
            }

        try:
            body = json.loads(event["body"])
        except json.JSONDecodeError:
            return {
                "statusCode": 400,
                "body": json.dumps({
                    "status": "FAILED",
                    "message": "Invalid JSON."
                })
            }
        logger.info(f"Incoming Transaction: {body}")


        missing = [field for field in REQUIRED_FIELDS if field not in body or str(body[field]).strip() == ""]

        if missing:
            return {
                "statusCode": 400,
                "body": json.dumps({
                    "status": "FAILED",
                    "missing_fields": missing
                })
            }
        try:
            amount = float(body["amount"])

            if amount <= 0:
                return {
                    "statusCode": 400,
                    "body": json.dumps({
                        "status": "FAILED",
                        "message": "Amount must be greater than zero."
                    })
                }

        except ValueError (ValueError, TypeError):
            return {
                "statusCode": 400,
                "body": json.dumps({
                    "status": "FAILED",
                    "message": "Invalid amount."
                })
            }
        logger.info(f"Sending transaction {body['transaction_id']} to SQS")
        response = sqs.send_message(
            QueueUrl=QUEUE_URL,
            MessageBody=json.dumps(body),
            MessageGroupId=body["customer_id"],
             MessageDeduplicationId=body["transaction_id"]
        )
        logger.info(f"SQS MessageId: {response['MessageId']}")
        logger.info("Message successfully sent to SQS")
        logger.info("API Lambda Completed Successfully")

        return {
            "statusCode": 202,
            "body": json.dumps({
                "status": "SUCCESS",
                "message": "Transaction accepted for processing",
                "transaction_id": body["transaction_id"]
            })
        }

    except Exception as e:

        logger.exception(e)

        return {
            "statusCode": 500,
            "body": json.dumps({
                "status": "FAILED",
                "message": "Internal Server Error"
            })
        }