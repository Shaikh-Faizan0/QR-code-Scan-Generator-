var1=1
var2=2
var3=int(input(" 1 For generat the QR code\n 2 For read the QR code \n Enter :"))

if var1==var3:
    # qrcode is a module of maker qrcode
    import qrcode

    # For taking the data from the user
    img = qrcode.make(input("data:"))
    # the qr code save as a image of name given my user input
    name = input("Name of QR code img:")
    img.save(f"{name}.jpg")
elif var2==var3:
    import cv2
    # cv2 is a module for opencv function
    from pyzbar.pyzbar import decode
    # pyzbar is a module for scane the QR code
    from warnings import filterwarnings

    filterwarnings('ignore')

    # Capture the video from default camera
    capture = cv2.VideoCapture(0)

    print("Escape Key (Esc) to exit...")

    recieved_data = None
    # if recieved date is none then do nothing
    while True:
        # reading frame from the camera
        _, frame = capture.read()
        # Decoding the QR Code
        decoded_data = decode(frame)
        try:
            data = decoded_data[0][0]
            if data != recieved_data:
                recieved_data = data
                # if date is recived data then print the data
                print("\n", data, "\n")

        except:
            pass

        # Showing video.
        cv2.imshow("QR CODE Scanner", frame)
        # To exit press Esc Key.
        key = cv2.waitKey(1)
        if key == 27:
            break

