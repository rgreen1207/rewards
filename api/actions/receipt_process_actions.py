import re
import json
import math

from uuid import uuid4
from datetime import date

from database import database_object
from api.models import ReceiptDBModel

class ReceiptProcessActions:
    
    @classmethod
    def process_receipt(cls, receipt):
        new_receipt = ReceiptDBModel(
            **json.loads(receipt.model_dump_json()),
            id = cls.generate_receipt_id(),
            points = cls.get_points(receipt),
        )
        cls.save_receipt(new_receipt)
        return new_receipt.id
    
    @classmethod
    def get_points(cls, receipt):
        points = 0
        points += cls.process_retailer_points(receipt.retailer)
        points += cls.process_item_points(receipt.items)
        points += cls.process_receipt_total_points(receipt.total)
        points += cls.process_date_points(receipt.purchaseDate)
        points += cls.process_time_points(receipt.purchaseTime)
        return points
    
    @staticmethod
    def save_receipt(receipt):    
        """
        normally, the model would dump to a JSON object with each key being the column name
        later, when the items are retrieved as a JSON object, it would be loaded back into the model
        in this case the full model is being saved for simplicity     
        """
        database_object[str(receipt.id)] = receipt
    
    @staticmethod
    def generate_receipt_id():
        return uuid4()
    
    @staticmethod
    def process_retailer_points(retailer):
        #remove punctuation and spaces, return length
        retailer = re.sub(r'[^a-zA-Z0-9]', '', retailer)
        return len(retailer) 

    @staticmethod
    def process_item_points(items):
        if len(items) == 0:
            return 0
        points = (len(items)//2)*5 #5 points for every 2 items
        for item in items:
            item_name = item.shortDescription.strip() #remove leading and trailing spaces
            if len(item_name) % 3 == 0:
                points += math.ceil(item.price * .2) #points equal to 20% of the price rounded up
        return points
    
    @staticmethod
    def process_receipt_total_points(total):
        points = 0
        if (total % 1) == 00: #whole dollar amount
            points += 50
        if (total % 1) % .25 == 0: #evenly divisible by .25
            points += 25
        return points
    
    @staticmethod
    def process_date_points(purchase_date):
        # 0 points for even days, 6 points for odd days
        return 0 if date.fromisoformat(purchase_date).day % 2 == 0 else 6
    
    
    @staticmethod
    def process_time_points(time):
        # 10 points for purchases between 2pm and 4pm
        time_split = time.split(':')
        return 10 if int(time_split[0]) in range(14, 16) else 0
