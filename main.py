#This is for addition of the private inputs of the 3 parties.
import sys 
import socket

sys.path.append( '/home/btv/Documents/sem5/PE-2022/add' )
sys.path.append( '/home/btv/Documents/sem5/PE-2022/Secret_Sharing' )

from add import Addition
from Reconstruction import Reconstruction


id = int(input())

f = open('/home/btv/Documents/sem5/PE-2022/add/coefficients.txt', "r")

c = [int(i) for i in f.read().split(" ")] #coefficients to which the inputs need to be multiplied and and added.
pub_val_path = '/home/btv/Documents/sem5/PE-2022/add/public_values.txt'


if(id==1):
    x1 = int(input())
    y1 = Addition(id,x1,c,pub_val_path)

    s = socket.socket()
    port = 12348
    s.bind(('', port))

    s.listen(5)  

    count = 0

    while True:
    
        c, addr = s.accept()    

        if count==0:
            y2 = c.recv(1024).decode()

            c.send(str(Reconstruction([int(y1),int(y2)],[3,4,5])).encode())
            c.close()

        elif count==1:

            c.send(str(Reconstruction([int(y1),int(y2)],[3,4,5])).encode())
            c.close()
    
        count += 1

        if count==2:
            break
    s.close()
    print(Reconstruction([int(y1),int(y2)],[3,4,5]))

elif(id==2):
    x2 = int(input())
    y2 = Addition(id,x2,c,pub_val_path)

    s = socket.socket()        
    port = 12348               
    s.connect(('127.0.0.1', port))
    s.send(str(y2).encode())

    out = s.recv(1024).decode()
    print(out)
    s.close() 

elif(id==3):
    x3 = int(input())
    y3 = Addition(id,x3,c,pub_val_path)

    s = socket.socket()        
    port = 12348               
    s.connect(('127.0.0.1', port))
    
    out = s.recv(1024).decode()
    print(out)
    s.close() 

else:
    print("Please enter a valid id!!")

