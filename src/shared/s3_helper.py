import json
import boto3

s3 = boto3.client("s3")


class S3Helper:

    @staticmethod
    def archive(bucket, transaction):

        key = (
            f"transactions/"
            f"{transaction['transaction_id']}.json"
        )

        s3.put_object(
            Bucket=bucket,
            Key=key,
            Body=json.dumps(transaction),
            ContentType="application/json"
        )

        return key