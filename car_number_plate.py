import cv2
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def highlight_car_number(image_path):
    try:
        with open(image_path, 'rb'):
            pass
        img = cv2.imread(image_path)
        if img is None:
            raise Exception("Error: Unable to read the image. Please check the file path.")
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blurred_img = cv2.GaussianBlur(gray_img, (5, 5), 0)
        edges = cv2.Canny(blurred_img, 100, 200)
        contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        largest_contour = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(largest_contour)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        number_plate_roi = gray_img[y:y + h, x:x + w]
        number_plate_text = pytesseract.image_to_string(Image.fromarray(number_plate_roi))
        print(f"Extracted Number Plate Text:{number_plate_text}")
        window_scale = 0.6  
        resized_img = cv2.resize(img, None, fx=window_scale, fy=window_scale, interpolation=cv2.INTER_LINEAR)
        cv2.imshow("Highlighted Car Number", resized_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except FileNotFoundError:
        print("Error: File not found. Please check the file path.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    image_path = input("Enter the path to the image: ").strip('\"')
    highlight_car_number(image_path)
