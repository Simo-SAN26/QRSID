import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image

print ("""                                                                                                              
                                                                                                              
     QQQQQQQQQ           RRRRRRRRRRRRRRRRR           SSSSSSSSSSSSSSS      IIIIIIIIII     DDDDDDDDDDDDD        
   QQ:::::::::QQ         R::::::::::::::::R        SS:::::::::::::::S     I::::::::I     D::::::::::::DDD     
 QQ:::::::::::::QQ       R::::::RRRRRR:::::R      S:::::SSSSSS::::::S     I::::::::I     D:::::::::::::::DD   
Q:::::::QQQ:::::::Q      RR:::::R     R:::::R     S:::::S     SSSSSSS     II::::::II     DDD:::::DDDDD:::::D  
Q::::::O   Q::::::Q        R::::R     R:::::R     S:::::S                   I::::I         D:::::D    D:::::D 
Q:::::O     Q:::::Q        R::::R     R:::::R     S:::::S                   I::::I         D:::::D     D:::::D
Q:::::O     Q:::::Q        R::::RRRRRR:::::R       S::::SSSS                I::::I         D:::::D     D:::::D
Q:::::O     Q:::::Q        R:::::::::::::RR         SS::::::SSSSS           I::::I         D:::::D     D:::::D
Q:::::O     Q:::::Q        R::::RRRRRR:::::R          SSS::::::::SS         I::::I         D:::::D     D:::::D
Q:::::O     Q:::::Q        R::::R     R:::::R            SSSSSS::::S        I::::I         D:::::D     D:::::D
Q:::::O  QQQQ:::::Q        R::::R     R:::::R                 S:::::S       I::::I         D:::::D     D:::::D
Q::::::O Q::::::::Q        R::::R     R:::::R                 S:::::S       I::::I         D:::::D    D:::::D 
Q:::::::QQ::::::::Q      RR:::::R     R:::::R     SSSSSSS     S:::::S     II::::::II     DDD:::::DDDDD:::::D  
 QQ::::::::::::::Q       R::::::R     R:::::R     S::::::SSSSSS:::::S     I::::::::I     D:::::::::::::::DD   
   QQ:::::::::::Q        R::::::R     R:::::R     S:::::::::::::::SS      I::::::::I     D::::::::::::DDD     
     QQQQQQQQ::::QQ      RRRRRRRR     RRRRRRR      SSSSSSSSSSSSSSS        IIIIIIIIII     DDDDDDDDDDDDD        
             Q:::::Q                                                                                          
              QQQQQQ                                                                                          
                                                                                                              
                                                                                                              
                                                                                                              
                                                                                                              
                                                                                                              """)

print("Create your QRSID identity\n")

name = input("Name: ")
surname = input("Surname: ")
date_of_birth = input("Date Of Birth (dd/mm/yyyy): ")
sex = input("Sex (Male, Famele, Non Binary): ")
city = input("City: ")
place_of_birth = input("Place Of Birty: ")

qr = pyqrcode.create("Name: {} | Surname: {} | Date Of Birth: {} | Sex: {} | City: {} | Place Of Birth: {}".format(name,surname,date_of_birth,sex,city,place_of_birth) )

print("\nYour QRSID was created successfully!\n")

qr.png("MY-QRSID.png", scale=8)
