import json
import boto3

secrets_client = boto3.client("secretsmanager")


class SecretHelper:

    @staticmethod
    def get_secret(secret_name):

        response = secrets_client.get_secret_value(
            SecretId=secret_name
        )

        return json.loads(
            response["SecretString"]
        )