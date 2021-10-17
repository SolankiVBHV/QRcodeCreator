from PIL import Image
from datetime import datetime
import qrcode
# from qrcode.main import QRCode


def generate_QR_Code(inData):
    #background image path and settings 
    logo_link = "BackLogo.jpg"
    logo = Image.open(logo_link)
    basewidth = 100

    # fixing background image as per QR code size 
    wpercent = (basewidth/float(logo.size[0]))
    hsize = int((float(logo.size[1])*float(wpercent)))
    logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
    QRcode = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H
    )

    # addingg URL or text to QRcode
    QRcode.add_data(inData)
    # generating QR code
    QRcode.make()
    # taking color name from user
    QRcolor = 'Blue'
    CiscoBlue = (0,186, 233)
    QRcolorBlack = 'Black'

    QRimg = QRcode.make_image(
        fill_color=QRcolorBlack, back_color="white").convert('RGB')

    pos = ((QRimg.size[0] - logo.size[0]) // 2,
        (QRimg.size[1] - logo.size[1]) // 2)
    QRimg.paste(logo, pos)
    imageName = "QR_Code_"+str(datetime.now()).split(".")[0].replace(' ','_').replace(':','_') + ".png"
    QRimg.save(imageName)

# test runner code 
# generate_QR_Code("test")