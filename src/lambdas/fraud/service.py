from shared.secret_helper import SecretHelper


class FraudService:

    @staticmethod
    def check(transaction):

        secret = SecretHelper.get_secret(
            "banking/application"
        )

        fraud_limit = secret["fraud_amount_limit"]

        amount = float(transaction["amount"])

        if amount > fraud_limit:

            return {
                "status": "FRAUD",
                "reason": f"Amount exceeds limit ({fraud_limit})"
            }

        if transaction["currency"] != "INR":

            return {
                "status": "REVIEW",
                "reason": "Foreign Currency"
            }

        blacklist = [
            "Fake Store",
            "Scam Merchant",
            "Dark Market"
        ]

        if transaction["merchant"] in blacklist:

            return {
                "status": "FRAUD",
                "reason": "Blacklisted Merchant"
            }

        return {
            "status": "APPROVED"
        }