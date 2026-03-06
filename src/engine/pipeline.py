from src.engine.extractor import ReceiptExtractor
from src.engine.parser import ReceiptParser


class ReceiptEngine:

    def __init__(self):
        self.extractor = ReceiptExtractor()
        self.parser = ReceiptParser()

    def process(self, image_path: str):

        raw_text = self.extractor.extract(image_path)

        receipt = self.parser.parse(raw_text)

        return receipt