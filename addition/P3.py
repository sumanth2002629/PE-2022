import sys
import random
import socket

sys.path.append( '/home/btv/Documents/sem5/PE-2022/Secret_Sharing' )
sys.path.append( '/home/btv/Documents/sem5/PE-2022' )

from Sharing import Sh
from field import Field


inp3 = 7

f = open("public_values.txt", "r")
public_values = [int(i) for i in f.read().split(" ")]

x31,x32,x33 = Sh(public_values,inp3)


#acting a sclient ot connect with P1
s = socket.socket()        
port = 12345               
s.connect(('127.0.0.1', port))
s.send(str(x31).encode())
x13 = s.recv(1024).decode()
s.close()  

#acting a sclient ot connect with P2
s = socket.socket()        
port = 12346               
s.connect(('127.0.0.1', port))
s.send(str(x32).encode())
x23 = s.recv(1024).decode()
s.close()


f = Field(997)
y3 = f.add(int(x13),f.add(int(x23),int(x33)))

s = socket.socket()        
port = 12347               
s.connect(('127.0.0.1', port))
s.send(str(y3).encode())

print("y3",y3)