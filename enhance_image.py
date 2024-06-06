import cv2
from PIL import Image, ImageEnhance
from paddleocr import PPStructure, save_structure_res

def enhance_image(image_path, output_path):
    # Step 1: Read the image using OpenCV
    print(image_path)
    image = cv2.imread(image_path)
    print(image)

    # Step 2: Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Step 3: Apply CLAHE (Contrast Limited Adaptive Histogram Equalization)
    clahe = cv2.createCLAHE(clipLimit=5.0, tileGridSize=(50, 50))
    enhanced_gray = clahe.apply(gray)

    # Step 4: Convert back to BGR color space
    enhanced_image = cv2.cvtColor(enhanced_gray, cv2.COLOR_GRAY2BGR)

    # Step 5: Convert the OpenCV image (BGR) to PIL image (RGB)
    enhanced_image = cv2.cvtColor(enhanced_image, cv2.COLOR_BGR2RGB)
    pil_image = Image.fromarray(enhanced_image)

    # Step 6: Enhance the sharpness using Pillow
    enhancer = ImageEnhance.Sharpness(pil_image)
    enhanced_pil_image = enhancer.enhance(2.0)  # Increase sharpness

    # Save the enhanced image
    enhanced_pil_image.save(output_path)


# Example usage
# input_image_path = 'input_image.jpg'
# output_image_path = 'enhanced_image.jpg'
# enhance_image(input_image_path, output_image_path)

if __name__ == '__main__':
    enhance_image(r"E:\code\img2table\0.jpg", "output.png")
    table_engine = PPStructure(layout=False, show_log=True)
    save_folder = './output'
    img_path = "0.jpg"
    img = cv2.imread(img_path)
    result = table_engine(img)
    save_structure_res(result, save_folder, str("1"))

    img_path = "output.png"
    img = cv2.imread(img_path)
    result = table_engine(img)
    save_structure_res(result, save_folder, str("2"))
