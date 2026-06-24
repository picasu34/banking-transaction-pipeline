from pydantic import BaseModel
from decimal import Decimal
from datetime import datetime


class TransactionRequest(BaseModel):
    transaction_id: str
    customer_id: str
    account_number: str
    transaction_type: str
    amount: Decimal
    currency: str
    merchant: str
    channel: str
    timestamp: datetime