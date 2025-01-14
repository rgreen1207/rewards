from uuid import UUID, uuid4
from fastapi.testclient import TestClient

from main import app
from database import database_object
from api.models.receipt_models import ReceiptDBModel


client = TestClient(app)

test_receipt = {
    "retailer": "Target",
    "purchaseDate": "2022-01-01",
    "purchaseTime": "13:01",
    "items": [
        {
        "shortDescription": "Mountain Dew 12PK",
        "price": "6.49"
        },{
        "shortDescription": "Emils Cheese Pizza",
        "price": "12.25"
        },{
        "shortDescription": "Knorr Creamy Chicken",
        "price": "1.26"
        },{
        "shortDescription": "Doritos Nacho Cheese",
        "price": "3.35"
        },{
        "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
        "price": "12.00"
        }
    ],
    "total": "35.35"
}


def test_process_receipt():
    response = client.post("/receipts/process", json=test_receipt)
    assert response.status_code == 200
    assert "id" in response.json()
    assert isinstance(UUID(response.json()["id"]), UUID)
    
def test_get_receipt():
    receipt = ReceiptDBModel(
        id=uuid4(),
        points=28,
        **test_receipt
    )
    database_object[str(receipt.id)] = receipt
    response = client.get(f"/receipts/{str(receipt.id)}")
    assert response.status_code == 200
    assert "receipt" in response.json()
    assert response.json()["receipt"]["id"] == str(receipt.id)

def test_get_points():
    receipt = ReceiptDBModel(
        id=uuid4(),
        points=28,
        **test_receipt
    )
    database_object[str(receipt.id)] = receipt
    response = client.get(f"/receipts/{str(receipt.id)}/points")
    assert response.status_code == 200
    assert "points" in response.json()
    assert response.json()["points"] == receipt.points