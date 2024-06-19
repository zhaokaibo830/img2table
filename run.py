import os
import cv2
import os
from paddleocr import PPStructure, save_structure_res
import uvicorn
from fastapi import FastAPI, File, UploadFile, Form, Body
from excel2json import excel_to_json
import time
from img2table.document import Image
from img2table.ocr import PaddleOCR
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    content: str


@app.post("/api/img2table_file")
def img2table_file(file: UploadFile = File(...)):
    """
    传入的是表格图片文件
    :param file: 图片对象
    :return: 表格的json定义
    """
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


@app.post("/api/img2table")
def img2table(item: Item = Body(...)):
    """
    传入的是表格图片的存放路径
    :param item: 表格图片的存放路径
    :return: 表格的json定义
    """
    print(1111)
    print(item.content)
    ocr = PaddleOCR(lang="ch")
    doc = Image(item.content)
    doc.to_xlsx(dest="output.xlsx",
                ocr=ocr,
                implicit_rows=False,
                borderless_tables=False,
                min_confidence=50)
    excel_path = os.path.join("output.xlsx")
    return excel_to_json(excel_path)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8020)
