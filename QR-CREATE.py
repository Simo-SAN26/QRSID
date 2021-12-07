import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image
# import csv

name = "Mario"
surname = "Rossi"
date_of_birth = "01/01/2000"
sex = "maschio"
city = "Milano"
place_of_birth = "Carate Brianza (MB)"

qr = pyqrcode.create("Nome: {} | Cognome: {} | data di nascita: {} | sesso: {} | città: {} | luogo di nascita: {}".format(name,surname,date_of_birth,sex,city,place_of_birth) )

qr.png("qrcode.png", scale=8)
