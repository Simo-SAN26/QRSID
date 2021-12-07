import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image

name = input("Name: ")
surname = input("Surname: ")
date_of_birth = input("Date Of Birth (dd/mm/yyyy): ")
sex = input("Sex (Male, Famele, Non Binary): ")
city = input("City: ")
place_of_birth = input("Place Of Birty: ")

qr = pyqrcode.create("Name: {} | Surname: {} | Date Of Birth: {} | Sex: {} | City: {} | Place Of Birth: {}".format(name,surname,date_of_birth,sex,city,place_of_birth) )

print("\nThe QRSID code was created successfully!\n")

qr.png("MY-QRSID.png", scale=8)
