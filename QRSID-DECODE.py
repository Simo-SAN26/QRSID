import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image
import time
import sys

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

print("Decode your QRSID\n")

qr_decode = decode(Image.open("MY-QRSID.png"))

print("Loading: ")

animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

for i in range(len(animation)):
    time.sleep(0.2)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()

print("\n")

print ("QRSID successfully decoded")
print ("----")
print (qr_decode[0].data.decode ("ascii"))

print("\n")

input()
