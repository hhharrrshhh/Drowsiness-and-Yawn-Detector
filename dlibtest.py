import cv2
import dlib
import numpy as np

# Load test image
image = cv2.imread("test_image.jpg")

if image is None:
    print("Error: Could not load test image.")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = np.ascontiguousarray(gray, dtype=np.uint8)  # Ensure correct format

detector = dlib.get_frontal_face_detector()
faces = detector(gray, 0)

print(f"Faces detected: {len(faces)}")
cv2.imshow("Gray Image", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
