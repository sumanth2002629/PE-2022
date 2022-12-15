import sys
import random
import socket

sys.path.append('/home/btv/Documents/sem5/PE-2022/Secret_Sharing')
sys.path.append('/home/btv/Documents/sem5/PE-2022/add')


from Reconstruction import Reconstruction
from Sharing import Sh
from field import Field

def Addition(id,inp,coeff,public_path):

    f = open(public_path, "r")
    public_values = [int(i) for i in f.read().split(" ")]

    if (id==1):

        x11,x12,x13 = Sh(public_values,inp)
        s = socket.socket()
        port = 12345 
        s.bind(('', port))

        s.listen(5)  

        count = 0

        while True:
        
            c, addr = s.accept()    

            if count==0:
                x21 = c.recv(1024).decode()
                c.send(str(x12).encode())
                c.close()

            elif count==1:
                x31 = c.recv(1024).decode()
                c.send(str(x13).encode()) 
                c.close()
            
            count += 1

            if count==2:
                break
        s.close()


        f = Field(997)
        y1 = f.add(f.mul(coeff[0],int(x11)),f.add(f.mul(coeff[1],int(x21)),f.mul(coeff[2],int(x31))))
        
        return y1

    elif(id==2):

        x21,x22,x23 = Sh(public_values,inp)

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

            x32 = c.recv(1024).decode()
            c.send(str(x23).encode())
            c.close()
            break

        f = Field(997)
        y2 = f.add(f.mul(coeff[0],int(x12)),f.add(f.mul(coeff[1],int(x22)),f.mul(coeff[2],int(x32))))
        return y2

    elif(id==3):
        x31,x32,x33 = Sh(public_values,inp)


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
        y3 = f.add(f.mul(coeff[0],int(x13)),f.add(f.mul(coeff[1],int(x23)),f.mul(coeff[2],int(x33))))

        return y3