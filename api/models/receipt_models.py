from pydantic import BaseModel, Field
from uuid import UUID

class ItemModel(BaseModel):

    shortDescription: str = Field(..., example="Apple")
    price: float = Field(..., example=1.99)


class ReceiptPOSTModel(BaseModel):
    
    retailer: str = Field(..., example="Walmart")
    purchaseDate: str = Field(..., example="2021-01-01")
    purchaseTime: str = Field(..., example="12:00:00")
    items: list[ItemModel] = Field(..., example=[{"shortDescription": "Apple", "price": 1.99}], description="List of items purchased")
    total: float = Field(..., example=10.99, description="Total $ amount of the receipt in USD")


class ReceiptDBModel(ReceiptPOSTModel):

    id: UUID = Field(..., example="123e4567-e89b-12d3-a456-426614174000", description="Unique identifier for the receipt")
    points: int = Field(..., example=100, description="Points earned from the receipt")
