#https://pypi.org/project/qrcode/
import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    
)

qr.add_data('wa.me/573008841693')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("QR.png")