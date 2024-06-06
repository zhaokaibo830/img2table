import os
import cv2
from paddleocr import PPStructure, save_structure_res
import uvicorn
from fastapi import FastAPI, File, UploadFile
from excel2json import excel_to_json
import time
from img2table.document import Image
from img2table.ocr import PaddleOCR

app = FastAPI()

import os

@app.post("/api/img2table")
def img2table(file: UploadFile = File(...)):
    contents = file.file.read()
    # 这里可以处理文件，比如保存到磁盘或者进行进一步处理
    # print(file.filename)
    # print(contents)
    # print(type(contents))
    # with open(f"temp.png", "wb") as f:
    #     f.write(contents)
    # img_path = 'temp.png'
    ocr = PaddleOCR(lang="ch")
    doc = Image(contents)
    doc.to_xlsx(dest="output.xlsx",
                ocr=ocr,
                implicit_rows=False,
                borderless_tables=False,
                min_confidence=50)
    excel_path = os.path.join("output.xlsx")
    return excel_to_json(excel_path)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
