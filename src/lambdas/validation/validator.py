from decimal import Decimal
from datetime import datetime

from pydantic import BaseModel, Field


class TransactionRequest(BaseModel):

    transaction_id: str = Field(..., min_length=5)

    customer_id: str

    customer_name: str

    account_number: str

    transaction_type: str

    amount: Decimal = Field(..., gt=0)

    currency: str

    merchant: str

    channel: str

    branch: str

    timestamp: datetime