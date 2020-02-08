import socket
import os
import pyscreenshot as ps
s=socket.socket()
host=input(str("please enter the hostname "))
s.connect((host,8080))
print("Connect to chat server ")
while True:
   im=s.recv(1024**2)
   im=im.decode()
   print(host,f'>',im)
   msg=input('user > ')
   if msg=="exit" or msg =="quit":
      s.send(msg.encode())
      break
   elif msg=="screenshot":
      im=ps.grab()
      im.save('test.png')
      print("screenshot has been taken")
      print("it already store in ",os.getcwd())
   s.send(msg.encode())
   
   
