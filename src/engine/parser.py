from src.schemas.receipt_schema import Receipt, ReceiptItem


class ReceiptParser:

    def parse(self, raw_text: str) -> Receipt:

        items = [
            ReceiptItem(name="Coffee", price=2.5),
            ReceiptItem(name="Bread", price=1.2),
        ]

        receipt = Receipt(
            store="Circle K",
            date="2025-03-01",
            items=items,
            total=3.7
        )

        return receipt