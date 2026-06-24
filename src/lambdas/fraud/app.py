from shared.logger import logger
from lambdas.fraud.service import FraudService


def lambda_handler(event, context):

    logger.info("Fraud Lambda Started")
    

    try:

        logger.info(f"Incoming Transaction: {event}")

        result = FraudService.check(event)

        event["fraud_status"] = result["status"]
        event["fraud_reason"] = result.get("reason", "")

        logger.info(f"Fraud Check Result: {result}")

        logger.info("Fraud Lambda Completed Successfully")

        return event

    except Exception as e:

        logger.exception(e)

        raise