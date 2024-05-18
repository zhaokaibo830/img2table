import os
import cv2
from paddleocr import PPStructure, save_structure_res
import uvicorn
from fastapi import FastAPI, File, UploadFile
from excel2json import excel_to_json
import time

app = FastAPI()

import os
import shutil

count = 1


def remove_folder_if_exists(folder_path):
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        shutil.rmtree(folder_path)


@app.post("/api/img2table")
def img2table(file: UploadFile = File(...)):
    global count
    folder_path = f"output\{count}"

    contents = file.file.read()
    # 这里可以处理文件，比如保存到磁盘或者进行进一步处理
    print(file.filename)
    with open(f"temp.png", "wb") as f:
        f.write(contents)
    table_engine = PPStructure(layout=False, show_log=True)
    save_folder = './output'
    img_path = 'temp.png'
    img = cv2.imread(img_path)
    result = table_engine(img)
    save_structure_res(result, save_folder, str(count))
    count += 1
    dir_path = folder_path
    for file in os.listdir(dir_path):
        if file.split('.')[1] == "xlsx" or file.split('.')[1] == "xls":
            excel_path = os.path.join(dir_path, file)
            return excel_to_json(excel_path)


if __name__ == "__main__":
    remove_folder_if_exists(f"output")
    uvicorn.run(app, host="0.0.0.0", port=8000)
