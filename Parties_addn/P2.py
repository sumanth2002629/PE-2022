import sys
import socket            
 
sys.path.append('/home/btv/Desktop/PE-2022/Secret Sharing')
from Sharing import Sh



x_2 = 2
ss = Sh([3,4,5],x_2)

P1 = 12345
P3 = 12457 

x_21 = ss[0]
x_22 = ss[1]
x_23 = ss[2]

s = socket.socket()        
print ("Socket successfully created")
 
port = 12346             
 
s.bind(('', port))        
# print ("socket binded to %s" %(port))
 
# s.listen(5)    
# print ("socket is listening") 

s.connect(('127.0.0.1', P1))

x_12 = int(s.recv(1024).decode())
print(x_12)


s.close()    
