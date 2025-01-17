from pydantic import BaseModel, Field
from uuid import UUID
from .receipt_models import ReceiptDBModel

class UserDBModel(BaseModel):

    id: int = Field(..., example=1234)
    #receipts: list[ReceiptDBModel]
