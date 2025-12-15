from typing import Annotated
from fastapi import Path, APIRouter

router = APIRouter(prefix="/items", tags=["items"])


@router.get("/")
def list_items():
    return ["item_id1", "item_id2"]


@router.get("/{item_id}")
def get_item_by_id(item_id: Annotated[int, Path(ge=1)]):
    return {"item_id": item_id}
