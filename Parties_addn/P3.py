import sys
import socket            
 
sys.path.append('/home/btv/Desktop/PE-2022/Secret Sharing')
from Sharing import Sh

x_3 = 3
ss = Sh([3,4,5],x_3)

P1 = 12345
P2 = 12346

x_31 = ss[0]
x_32 = ss[1]
x_33 = ss[2]

port = 12347          
 
s = socket.socket()        
print ("Socket successfully created")

s.bind(('', port)) 

s.connect(('127.0.0.1', P1))

x_13 = int(s.recv(1024).decode())
print(x_13)

s.close()