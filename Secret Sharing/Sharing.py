import sys
import random

sys.path.append( '/home/btv/Desktop/PE-2022' )

from field import Field 

def Sh(public_inputs,secret):

    shares = []

    f = Field(997)
    coeff = random.randrange(997)

    for x in public_inputs:
        shares.append(f.add(secret,f.mul(coeff,x)))
    
    return shares

if __name__=="__main__":
    ss = Sh([3,4,5],5)
    print(ss)