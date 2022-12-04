import sys
sys.path.append('/home/btv/Documents/sem5/PE-2022')

from field import Field 


def Reconstruction(shares,public_inputs):

    if(len(shares) < 2):
        return print("Reconstruction not possible. Required atleast 2 shares")

    f = Field(997)

    num_term1 = f.mul(f.add_inv(public_inputs[1]),shares[0])
    den_term1 = f.add(public_inputs[0],f.add_inv(public_inputs[1]))

    term1 = f.mul(num_term1, f.mul_inv(den_term1))

    num_term2 = f.mul(f.add_inv(public_inputs[0]),shares[1])
    den_term2 = f.add(public_inputs[1],f.add_inv(public_inputs[0]))

    term2 = f.mul(num_term2, f.mul_inv(den_term2))

    return f.add(term1,term2)

    
if __name__=="__main__":
    print(Reconstruction([379,167],[3,4,5]))