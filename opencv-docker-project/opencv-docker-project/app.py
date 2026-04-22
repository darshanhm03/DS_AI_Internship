import cv2
import os

print("📂 Files inside container:", os.listdir())

# Load image
img = cv2.imread('input.jpeg')

# Check if image loaded
if img is None:
    print("❌ ERROR: input.jpeg not found!")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Gaussian Blur
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Edge detection
edges = cv2.Canny(blur, 100, 200)

# Save output
cv2.imwrite('output.jpeg', edges)

print("✅ Image processed successfully!")