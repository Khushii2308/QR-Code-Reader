# QR-Code-Reader
This is a simple Qr code reader in python that reads the qr from the provided image.
It Converts each image to grayscale using cv2.cvtColor() for QR code detection,Utilizes cv2.QRCodeDetector().detectAndDecode() to locate and decode QR codes within each image and returns the decoded data (qrcodes[0]), assuming each image contains a single QR code.
