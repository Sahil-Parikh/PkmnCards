import cv2
import pytesseract
from PIL import Image

# Set Tesseract path if not in your PATH environment variable
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_image(image, roi):
    """Extract text from a specified region of interest (ROI) in the image."""
    x, y, w, h = roi
    cropped_image = image[y:y+h, x:x+w]
    gray = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)
    text = pytesseract.image_to_string(thresh, lang="eng")
    return text.strip()

def identify_card_from_camera():
    """Identify card name, number, and set using the camera."""
    cap = cv2.VideoCapture(0)
    print("Press 'c' to capture an image or 'q' to quit.")

    card_info = {"name": None, "number": None, "set": None}
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture video.")
            break
        
        cv2.imshow("Card Recognition", frame)

        # Press 'c' to capture
        if cv2.waitKey(1) & 0xFF == ord('c'):
            # Define ROIs (Region of Interest) for card text
            # Adjust these coordinates based on card layout
            name_roi = (50, 20, 300, 50)  # Approximate name position
            number_roi = (20, 450, 100, 30)  # Approximate number position
            set_roi = (200, 450, 100, 30)  # Approximate set position

            # Extract text from the image
            card_info["name"] = extract_text_from_image(frame, name_roi)
            card_info["number"] = extract_text_from_image(frame, number_roi)
            card_info["set"] = extract_text_from_image(frame, set_roi)
            
            print("Card Information:")
            print(f"Name: {card_info['name']}")
            print(f"Number: {card_info['number']}")
            print(f"Set: {card_info['set']}")
            break

        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
    return card_info

if __name__ == "__main__":
    card_details = identify_card_from_camera()
    print("Identified Card:", card_details)
