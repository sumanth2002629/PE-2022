import sys
import random
import socket



sys.path.append( '/home/btv/Documents/sem5/PE-2022/Secret_Sharing' )
sys.path.append( '/home/btv/Documents/sem5/PE-2022' )

from field import Field
from Sharing import Sh

inp2 = 6

f = open("public_values.txt", "r")
public_values = [int(i) for i in f.read().split(" ")]

x21,x22,x23 = Sh(public_values,inp2)


#acting as a client to connect with P1 
s = socket.socket()        
port = 12345               
s.connect(('127.0.0.1', port))
s.send(str(x21).encode())
x12 = s.recv(1024).decode()
s.close()  

#acting as a server to connect with P3
s1 = socket.socket()
port = 12346 
s1.bind(('', port))
s1.listen(5) 

while True:
  c, addr = s1.accept()    
  print ('Got connection from', addr )

  x32 = c.recv(1024).decode()
  c.send(str(x23).encode())
  print("x32",x32)
  c.close()
  break


f = Field(997)
y2 = f.add(int(x12),f.add(int(x22),int(x32)))

s = socket.socket()        
port = 12347               
s.connect(('127.0.0.1', port))
s.send(str(y2).encode())

print("y2",y2)


