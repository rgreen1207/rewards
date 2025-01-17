from fastapi import HTTPException
from database import database_object_receipts

class ReceiptLookupActions:

    @staticmethod
    def get_receipt(receipt_id):
        try:
            return database_object_receipts[str(receipt_id)]
        except KeyError:
            raise HTTPException(status_code=404, detail= f"Receipt id: {receipt_id} not found")

    @classmethod
    def get_points(cls, receipt_id):
        return cls.get_receipt(receipt_id).points
    
    def get_all():
        return database_object_receipts