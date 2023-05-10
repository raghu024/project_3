class complek:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    def __add__(self,other):
        re=self.real+other.real
        im=self.imag+other.imag
        return(re,im)
s=complek(20,30)
p=complek(50,60)
x=complek(90,60)
print(s+p)

          
