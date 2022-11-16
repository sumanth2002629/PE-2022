import sys
import socket            
 
sys.path.append('/home/btv/Desktop/PE-2022/Secret Sharing')
from Sharing import Sh

P2 = 12346
P3 = 12347

x_1 = 1
ss = Sh([3,4,5],x_1)

s = socket.socket()        
print ("Socket successfully created")
 
port = 12345               
 
s.bind(('', port))        
print ("socket binded to %s" %(port))
 
s.listen(5)    
print ("socket is listening")    

x_11 = ss[0]
x_12 = ss[1]
x_13 = ss[2]
count = 0


while True:
 
  c, addr = s.accept()    
  print ('Got connection from', addr )

  if(addr[1] == P2):
    c.send(str(x_12).encode())
    count += 1
    c.close()

  elif(addr[1] == P3):
    c.send(str(x_13).encode())
    count +=1
    c.close()

  print(count)
  if(count >= 2):
    break


s.close()

