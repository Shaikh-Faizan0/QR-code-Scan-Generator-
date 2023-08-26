import qrcode
import sys
import cv2
from pyzbar.pyzbar import decode
from warnings import filterwarnings

# Suppress warnings
cv2.destroyAllWindows()
sys.tracebacklimit = 0

def generate_qr_code():
    data_to_encode = input("Enter the data you want to encode: ")

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data_to_encode)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    name = input("Name of QR code image: ")
    img.save(f"{name}.png")
    print("\nQR code generated successfully as", f"{name}.png")

def scan_qr_code():
    filterwarnings('ignore')
    capture = cv2.VideoCapture(0)

    print("Press the Escape Key (Esc) to exit...")

    received_data = None

    while True:
        _, frame = capture.read()
        decoded_data = decode(frame)
        try:
            data = decoded_data[0][0]
            if data != received_data:
                received_data = data
                print("\nDecoded QR code data:", data, "\n")
                break  # Exit the loop when data is received

        except IndexError:
            pass

        cv2.imshow("QR Code Scanner", frame)
        key = cv2.waitKey(1)
        if key == 27:
            break
    print("Thank you for using the QR Code Generator and Scanner!")
    capture.release()
    cv2.destroyAllWindows()

print("=" * 40)
print("{:^40}".format("QR Code Generator and Scanner"))
print("=" * 40)

print("Welcome to QR Code Generator and Scanner!")
print("1. Generate QR Code")
print("2. Scan QR Code")


while True:
    try:
        choice = int(input("Enter your choice (1/2): "))
        if choice not in [1, 2]:
            print("Invalid choice. Please enter 1 or 2.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if choice == 1:
    generate_qr_code()
elif choice == 2:
    scan_qr_code()

print("=" * 55)
print("{:^40}".format("Thank you for using the QR Code Generator and Scanner!"))
print("=" * 55)
