import wolframalpha
import pandas as pd
import os
import socket
import wikipedia
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostbyname(socket.gethostname())
print("server will start on host : ",host)
s.bind((host,8080))
s.listen(5)
clientsocket,addres=s.accept()
print(addres," has connected to the server and online ")
a=pd.read_csv("script.csv")
quest=list(a['query'].values)
ans=list(a['answer'].values)
client=wolframalpha.Client('JTELP6-P3E4VG4RKA')
clientsocket.send("write your query".encode())
while True:
    try:
        i=clientsocket.recv(1024**2)
        i=i.decode()
        print("user > ",i)
        if i=="":
            clientsocket.send("please say something".encode())
        else:
            count=0
            for x,y in enumerate(quest):
                if y==i:
                    print('ganos > ',ans[x])
                    clientsocket.send(ans[x].encode())
                    break
        
        
        if i=="exit" or i=="quit" or i=="close":
            print("thank you for using ".title())
            msg="thank you for using"
            clientsocket.send(msg.encode())
            break
        if i not in quest:
                res=client.query(i)
                ans1=next(res.results).text
                print('ganos > ',ans1)
                clientsocket.send(ans1.encode())
    except:
        try:
            wiki=wikepedia.summary(i)
            clientsocket.send(wiki.encode())
            print("something worng")
        except:
            clientsocket.send("we are having problem ,no need to warry our crazy programmer will handle".encode())
            
