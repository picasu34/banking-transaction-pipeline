import json

from shared.logger import log


def lambda_handler(event, context):

    log(
        "INFO",
        "AuditLambda",
        "Audit event received",
        event=event
    )

    detail = event.get("detail", {})

    log(
        "INFO",
        "AuditLambda",
        "Transaction audited",
        transaction_id=detail.get("transaction_id"),
        customer_id=detail.get("customer_id"),
        fraud_status=detail.get("fraud_status")
    )

    return {
        "statusCode": 200
    }