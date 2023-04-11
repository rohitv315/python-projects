# istall the qrcode by using the command pip install qrcode and image by using pip install image


import qrcode
import image

qr=qrcode.QRCode(
    version=15,
    box_size=10,
    border=5
)

data="https://www.youtube.com/"    # we can give the string or the link where after scanning the qr code you will get the output.

qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="black",back_colour="white")
img.save("test.png")     


#after running it you will get the test.ong image where you will get qr code
