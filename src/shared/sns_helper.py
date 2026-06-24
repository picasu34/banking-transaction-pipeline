import os
import boto3

sns = boto3.client("sns")

TOPIC_ARN = os.environ["TOPIC_ARN"]


class SNSHelper:

    @staticmethod
    def publish(subject, message):

        return sns.publish(
            TopicArn=TOPIC_ARN,
            Subject=subject,
            Message=message
        )