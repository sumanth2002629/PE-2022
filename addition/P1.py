import sys
import random
import socket

sys.path.append( '/home/btv/Documents/sem5/PE-2022' )
sys.path.append( '/home/btv/Documents/sem5/PE-2022/Secret_Sharing' )


from field import Field
from Sharing import Sh
from Reconstruction import Reconstruction

inp1 = 5

f = open("public_values.txt", "r")
public_values = [int(i) for i in f.read().split(" ")]

x11,x12,x13 = Sh(public_values,inp1)

s = socket.socket()
port = 12345 
s.bind(('', port))

s.listen(5)  

count = 0

while True:
 
  c, addr = s.accept()    
  print ('Got connection from', addr )

  if count==0:
    x21 = c.recv(1024).decode()
    c.send(str(x12).encode())
    print("x21",x21)
    c.close()

  elif count==1:
    x31 = c.recv(1024).decode()
    c.send(str(x13).encode())
    print("x31",x31) 
    c.close()
  
  count += 1

  if count==2:
    break
s.close()


f = Field(997)
y1 = f.add(int(x11),f.add(int(x21),int(x31)))


#getting output shares from P2 and P3
s = socket.socket()
port = 12347
s.bind(('', port))

s.listen(5)  

count = 0

while True:
 
  c, addr = s.accept()    
  print ('Got connection from', addr )

  if count==0:
    y2 = c.recv(1024).decode()
    c.close()
  elif count==1:
    y3 = c.recv(1024).decode() 
    c.close()
  count += 1
  if count==2:
    break

file = open("result.txt","w")
file.write(str(Reconstruction([int(y1),int(y2)],public_values)))

