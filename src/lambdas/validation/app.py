import json

from shared.logger import logger
from shared.response import success_response
from shared.response import error_response

from lambdas.validation.service import ValidationService
from shared.sqs_helper import SQSHelper


def lambda_handler(event, context):

    logger.info("Validation Lambda Started")

    try:

        # API Gateway invocation
        if "body" in event:

            body = json.loads(event["body"])

            transaction = ValidationService.process(body)

            SQSHelper.send_message(
                transaction.model_dump(mode="json")
            )

            return success_response(
                "Validation Successful",
                transaction.model_dump(mode="json")
            )

        # Step Function invocation
        else:

            transaction = ValidationService.process(event)

            return transaction.model_dump(mode="json")

    except Exception as e:

        logger.exception(e)

        return error_response("Internal Server Error")