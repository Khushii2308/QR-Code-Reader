import cv2
import numpy as np

def decode(image1):
  # Convert the image to grayscale
  gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

  # Detect QR codes in the image
  qrcodes = cv2.QRCodeDetector().detectAndDecode(gray)

  # Return the decoded data
  return qrcodes[0]
def decode(image2):
  # Convert the image to grayscale
  gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

  # Detect QR codes in the image
  qrcodes = cv2.QRCodeDetector().detectAndDecode(gray)

  # Return the decoded data
  return qrcodes[0]
# Read the image
image1 = cv2.imread("qr.jpg")
image2 = cv2.imread("qr2.jpg")

# Decode the QR code
data1 = decode(image1)
data2 = decode(image2)

# Print the decoded data
print(data1)
print(data2)