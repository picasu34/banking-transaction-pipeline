from shared.logger import log
from shared.sns_helper import SNSHelper


def lambda_handler(event, context):

    log(
        "ERROR",
        "FailureLambda",
        "Workflow failed",
        error=str(event)
    )

    SNSHelper.publish(
        subject="Banking Workflow Failed",
        message=f"""
Workflow Failure Detected

Execution Details:

{event}
"""
    )

    return {
        "status": "FAILED"
    }