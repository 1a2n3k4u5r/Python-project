import qrcode

img = qrcode.make("https://www.google.com")
img.save("google_qr.png")

print("QR Code created successfully!")
