import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image
# import csv

nome = "Mario"
cognome = "Rossi"
dataDiNascita = "01/01/2000"
sesso = "maschio"
città = "Milano"
luogoDiNascita = "Carate Brianza (MB)"

qr = pyqrcode.create("Nome: {} | Cognome: {} | data di nascita: {} | sesso: {} | città: {} | luogo di nascita: {}".format(nome,cognome,dataDiNascita,sesso,città,luogoDiNascita) )

qr.png("qrcode.png", scale=8)
