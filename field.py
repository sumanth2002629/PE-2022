class Field:
    def __init__(self,p):
        self.p = p

    def add(self,x,y):
        return (x+y)%self.p

    def mul(self,x,y):
        return (x*y)%self.p
    
    def add_inv(self,x):
        return self.p - (x%self.p)

    def mul_inv(self,x):  #computed using fermats little thm. x^(p-1) = 1  (over mod p)
        y = self.p-2

        res = 1
 
        while (y > 0):
 
            if ((y & 1) != 0):
                res = res * x % self.p
 
            y = y >> 1 
            x = x * x % self.p  
 
        return res % self.p


if __name__=="__main__":
    f = Field(997)

    print(f.add_inv(10))
    print(f.mul_inv(10))
