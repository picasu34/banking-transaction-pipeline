from lambdas.validation.validator import TransactionRequest


class ValidationService:

    @staticmethod
    def process(body):

        transaction = TransactionRequest(**body)

        return transaction