import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask


s=input("Enter the text of whose QR code you would like to generate: ")
v=input("Enter the detailing in your QR code that you want in scale of 1-40: ")
b=input("Enter the box size of each box in the QR code in pixel: ")
bo=input("Enter the border size of the QR code: ")

qr = qrcode.QRCode(
    version=v,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=b,
    border=bo,
)

qr.add_data(s)
qr.make(fit=True)

img = qr.make_image(fill_color="#FF1700", back_color="#041C32")

img.save("custom_qr.png") #this will be the qr whose color u have defined

img_1 = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer()) #this will have rounded border

img_2 = qr.make_image(image_factory=StyledPilImage, color_mask=RadialGradiantColorMask()) #this will have a radiant color effect

img_3 = qr.make_image(image_factory=StyledPilImage, embeded_image_path="17moons.png") #you can embedd your custom png by just replacing the name of file and copying the png the code folder


img_1.save("rounded_qr.png")
img_2.save("radiant_qr.png")
img_3.save("embed_img_qr.png")
