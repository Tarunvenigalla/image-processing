import pytesseract
from PIL import Image

# Replace this path with the path to your Tesseract installation
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_image(image_path):
    try:
        # Open the image file
        with Image.open(image_path) as img:
            # Perform OCR on the image
            text = pytesseract.image_to_string(img)

            # Print the extracted text
            print(f"Extracted Text:{text}")
            #print(text)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    image_path = r"C:\Users\tarun\OneDrive\Desktop\code\image-processing\images\image5.jpeg"
    extract_text_from_image(image_path)
