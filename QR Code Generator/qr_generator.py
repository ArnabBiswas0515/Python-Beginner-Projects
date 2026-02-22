import qrcode

user_input_data = input("Enter the text ot URL: ").strip()
filename = input("Enter the filename: ").strip()

qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(user_input_data)
image = qr.make_image(fill_color="black", back_color="white")
image.save(filename)

print(f"QR Code saved as {filename}")