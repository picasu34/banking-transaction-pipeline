import os

AWS_REGION = os.getenv("AWS_REGION", "ap-south-1")

RAW_BUCKET = os.getenv(
    "RAW_BUCKET",
    "banking-raw-data"
)

QUEUE_NAME = os.getenv(
    "QUEUE_NAME",
    "bank-transaction-queue.fifo"
)

TABLE_NAME = os.getenv(
    "TABLE_NAME",
    "BankTransactionStatus"
)

MAX_TRANSACTION_AMOUNT = 1000000

SUPPORTED_CURRENCIES = [
    "INR",
    "USD",
    "EUR"
]

SUPPORTED_CHANNELS = [
    "UPI",
    "ATM",
    "CARD",
    "NETBANKING"
]

TRANSACTION_TYPES = [
    "DEBIT",
    "CREDIT"
]