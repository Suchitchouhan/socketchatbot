import wolframalpha
import pandas as pd
import os
import socket
import wikipedia
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostbyname(socket.gethostname())
print("server will start on host : ",host)
s.bind((host,5000))
s.listen(5)
clientsocket,addres=s.accept()
print(addres," has connected to the server and online ")
a=pd.read_csv("script.csv")
quest=list(a['query'].values)
ans=list(a['answer'].values)
client=wolframalpha.Client('JTELP6-P3E4VG4RKA')
clientsocket.send("write your query".encode())
def phonedetails(az):
       try:     
             x = phonenumbers.parse(az, None)
             ro = phonenumbers.parse(az, "RO")
             gb = phonenumbers.parse(az, "GB")
             az1=ro
             az2=geocoder.description_for_number(x, "en")
             az3=carrier.name_for_number(ro, "en")
             az4=timezone.time_zones_for_number(gb)
             return str(az1)+'\n'+'country : '+str(az2)+'\n'+'Service provider : '+str(az3)+'\n'+'time Zone : '+str(az4)
       except:
              return "we could not able give infomation"
def stringcleaner(x):
     b=a.split(" ")
     c=list('[@_!#$%^&*()<>?/\|}{~:]')
     for x in c:
        if x in b:
            b.remove(x)
     for x in b:
         if len(x)==0:
            b.remove(x)
     return ' '.join(b)
def wolfmalf(i):
       res=client.query(i)
       ans1=next(res.results).text
       print('ganos > ',ans1)
       ans1=ans1.split(".")
       ans1='\n'.join(ans1)
       return ans1
       

while True:
    try:
        i=clientsocket.recv(1024**2)
        i=i.decode()
        i=stringcleaner(i)
        print("user > ",i)
        a=i.split(" ")
        if i=="":
            clientsocket.send("please say something".encode())
        else:
            count=0
            for x,y in enumerate(quest):
                if y==i:
                    print('ganos > ',ans[x])
                    clientsocket.send(ans[x].encode())
                    break
        if 'phone' and 'detail' in a:
              clientsocket.send("Please enter mobile number with country code ".encode())
              i=clientsocket.recv(1024**2)
              i=i.decode()
              i='+'+i
              clientsocket.send(phonedetails(i).encode())

              

        if i=="exit" or i=="quit" or i=="close":
            print("thank you for using ".title())
            msg="thank you for using"
            clientsocket.send(msg.encode())
            clientsocket.close()
            break
        if i not in quest:
                ans12=wolfmalf(i)
                clientsocket.send(ans12.encode())       
                
    except:
        try:
            b=wikipedia.summary(i)
            clientsocket.send(b.encode())
            print("something worng")
        except:
            
            clientsocket.send("we are having problem ,no need to warry our crazy programmer will handle".encode())
            
