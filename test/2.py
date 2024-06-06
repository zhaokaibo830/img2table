from img2table.document import Image

# Instantiation of OCR
from img2table.ocr import PaddleOCR

ocr = PaddleOCR(lang="ch")

# Instantiation of document, either an image or a PDF
doc = Image("16.png")

# Extraction of tables and creation of a xlsx file containing tables
doc.to_xlsx(dest="16.xlsx",
            ocr=ocr,
            implicit_rows=True,
            borderless_tables=True,
            min_confidence=1)
