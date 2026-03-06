from dataclasses import dataclass
from typing import List


@dataclass
class ReceiptItem:
    name: str
    price: float


@dataclass
class Receipt:
    store: str
    date: str
    items: List[ReceiptItem]
    total: float