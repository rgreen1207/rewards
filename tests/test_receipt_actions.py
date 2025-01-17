from api.actions.receipt_process_actions import ReceiptProcessActions
from api.models.receipt_models import ItemModel

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



def test_process_retailer_points():
    test_params = {
        test_receipt["retailer"]: 6,
        "Walmart": 7,
        "Walmart!": 7,
        "asidfjaosdifj": 13,
        "!!!!": 0,
    }
    for retailer, points in test_params.items():
        assert ReceiptProcessActions.process_retailer_points(retailer) == points

def test_process_receipt_total_points():
    test_params = {
        float(test_receipt["total"]): 0,
        10.00: 75,
        10.25: 25,
    }

    for total, points in test_params.items():
        assert ReceiptProcessActions.process_receipt_total_points(total) == points

def test_process_item_points():
    itemList = [ItemModel(**item) for item in test_receipt["items"]]
    assert ReceiptProcessActions.process_item_points(itemList) == 16
    assert ReceiptProcessActions.process_item_points([]) == 0


def test_process_date_points():
    test_params = {
        test_receipt["purchaseDate"]: 6,
        "2022-12-31": 6,
        "2022-02-28": 0
    }

    for date, points in test_params.items():
        assert ReceiptProcessActions.process_date_points(date) == points

def test_process_time_points():
    test_params = {
        test_receipt["purchaseTime"]: 0,
        "14:00": 10,
        "16:00": 0,
        "15:59": 10,
    }

    for time, points in test_params.items():
        assert ReceiptProcessActions.process_time_points(time) == points
