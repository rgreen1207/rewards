from uuid import UUID
from fastapi.routing import APIRouter
from fastapi.param_functions import Body

from api.models import ReceiptPOSTModel
from api.actions import ReceiptProcessActions, ReceiptLookupActions

router = APIRouter(prefix="/receipts", tags=["receipts"])

@router.post("/process")
def process_receipt(receipt: ReceiptPOSTModel = Body(...)):
    return {"id":  ReceiptProcessActions.process_receipt(receipt)}

@router.get("/{id}")
def get_receipt(id: UUID):
    return {"receipt":  ReceiptLookupActions.get_receipt(id)}

@router.get("/{id}/points")
def get_points(id: UUID):
    return {"points":  ReceiptLookupActions.get_points(id)}
