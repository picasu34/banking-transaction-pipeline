import json

from shared.logger import logger, log
from shared.sns_helper import SNSHelper

from lambdas.processor.service import ProcessorService
from lambdas.fraud.service import FraudService
from shared.eventbridge_helper import EventBridgeHelper
from shared.s3_helper import S3Helper
import os



def lambda_handler(event, context):

    log(
        "INFO",
        "ProcessorLambda",
        "Processor started"
    )

    if "Records" in event:

        transactions = [
            json.loads(record["body"])
            for record in event["Records"]
        ]

    # Step Function Invocation
    else:

        transactions = [event]

    for transaction in transactions:

        

        try:

            
            fraud_result = FraudService.check(transaction)
            transaction["fraud_status"] = fraud_result["status"]
            transaction["fraud_reason"] = fraud_result.get("reason", "")
            

            log(
                "INFO",
                "ProcessorLambda",
                "Transaction received",
                transaction_id=transaction["transaction_id"],
                customer_id=transaction["customer_id"],
                amount=transaction["amount"],
                currency=transaction["currency"]
            )

            log(
                "INFO",
                "ProcessorLambda",
                "Fraud analysis completed",
                transaction_id=transaction["transaction_id"],
                fraud_status=fraud_result["status"],
                fraud_reason=fraud_result.get("reason", "")
            )

            log(
                "INFO",
                "ProcessorLambda",
                "Processing transaction",
                transaction_id=transaction["transaction_id"],
                customer_id=transaction["customer_id"]
            )

            ProcessorService.process(transaction)
            ##dynamo db write successful
            log(
                "INFO",
                "ProcessorLambda",
                "Transaction saved",
                transaction_id=transaction["transaction_id"]
            )

            archive_key = S3Helper.archive(
                os.environ["ARCHIVE_BUCKET"],
                transaction
            )

            log(
                "INFO",
                "ProcessorLambda",
                "Transaction archived",
                transaction_id=transaction["transaction_id"],
                s3_key=archive_key
            )
            
            log(
                "INFO",
                "ProcessorLambda",
                "Publishing SNS notification",
                transaction_id=transaction["transaction_id"]
            )

            response = SNSHelper.publish(

                subject="Bank Transaction Processed",

                message=(
                    f"Transaction Successfully Processed\n\n"
                    f"Transaction ID : {transaction.get('transaction_id', 'N/A')}\n"
                    f"Customer ID    : {transaction.get('customer_id', 'N/A')}\n"
                    f"Customer Name  : {transaction.get('customer_name', 'N/A')}\n"
                    f"Account Number : {transaction.get('account_number', 'N/A')}\n"
                    f"Amount         : {transaction.get('amount', 'N/A')} {transaction.get('currency', '')}\n"
                    f"Merchant       : {transaction.get('merchant', 'N/A')}\n"
                    f"Channel        : {transaction.get('channel', 'N/A')}\n"
                    f"Branch         : {transaction.get('branch', 'N/A')}\n"
                    f"Transaction Type : {transaction.get('transaction_type','N/A')}\n\n"
                    f"Fraud Status   : {transaction['fraud_status']}\n"
                    f"Reason         : {transaction['fraud_reason']}"
                )
            )

            log(
                "INFO",
                "ProcessorLambda",
                "Notification sent",
                transaction_id=transaction["transaction_id"],
                message_id=response["MessageId"]
            )

            event_response = EventBridgeHelper.publish(transaction)

            log(
                "INFO",
                "ProcessorLambda",
                "EventBridge event published",
                transaction_id=transaction["transaction_id"]
            )
            

            

        except Exception as e:
            logger.exception(e)
            raise


    return {
        "statusCode": 200
    }