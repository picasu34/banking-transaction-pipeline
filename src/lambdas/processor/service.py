from lambdas.processor.repository import TransactionRepository


class ProcessorService:

    @staticmethod
    def process(transaction):

        TransactionRepository.save(transaction)