QR Code Generator and Scanner Program Documentation
==================================================

Introduction:
--------------
This Python program implements a QR Code Generator and Scanner. It allows users to either generate QR codes for given data or scan QR codes using their computer's camera. The program uses the 'qrcode', 'cv2' (OpenCV), and 'pyzbar' libraries to achieve its functionality.

Usage:
-------
1. Run the script using a Python interpreter.
2. The program displays a menu with two options: Generate QR Code or Scan QR Code.
3. Depending on the user's choice, they can generate a QR code with data they provide or scan QR codes from their camera feed.
4. The program provides clear instructions, guides users through the process, and displays relevant information.

Components and Features:
-------------------------
1. QR Code Generation:
   - Users can choose to generate a QR code.
   - They input the data they want to encode.
   - The program generates a QR code image and saves it.
   - The user specifies a name for the image.

2. QR Code Scanning:
   - Users can choose to scan QR codes.
   - The program captures video from the computer's camera.
   - It decodes QR codes present in the video frames using the 'pyzbar' library.
   - Successfully decoded QR code data is displayed separately.
   - The video feed stops when a QR code is successfully decoded.

3. User-Friendly Interface:
   - The program displays clear instructions and menu options.
   - Input validation ensures users enter valid choices.
   - Visual formatting with equal signs and centered headings enhances the interface.

4. Suppressed Warnings and Errors:
   - Warnings related to camera usage are suppressed to provide a cleaner interface.
   - Traceback information from errors is hidden for a more streamlined experience.

Usage Example:
---------------
1. User input: 1
   - User chooses to generate a QR code.
   - Enters data: "https://www.example.com"
   - Names the image: "example_qr_code"
   - Program generates the QR code image as "example_qr_code.png".
   - ![example_qr_code](https://github.com/faizan0111/QR-code-Scan-Generator-/assets/95975060/7ec4178e-8910-4fe8-a13b-564d1a158eb7)


2. User input: 2
   - User chooses to scan QR codes.
   - Video feed from the camera is displayed.
   - The user presents a QR code to the camera.
   - The program decodes the QR code and displays its data.

3. User exits the program using the provided exit option.

Author:
-------
This code was authored by Shaikh Faizan Shaikh Mohammed Iqbal. It is intended for educational and illustrative purposes.
