import json

def success_response(message, data=None):

    return {
        "statusCode": 200,
        "body": json.dumps({
            "status": "SUCCESS",
            "message": message,
            "data": data
        })
    }


def error_response(message):

    return {
        "statusCode": 400,
        "body": json.dumps({
            "status": "FAILED",
            "message": message
        })
    }