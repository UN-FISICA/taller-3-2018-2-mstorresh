import myfloat_func as my
class Decimales:
    def __init__(self, z): #parametro son las tuplas, enteros y decimales
        if (type(z) is int) or (type(z) is float):
            self.z=my.numtup(z)
        else:
            self.z=z
    def __add__(self,other):
        if isinstance(other,(int,float)):
            other = my.numtup(other)
            return Decimales(my.suma(self.z,other))
        if isinstance(other, Decimales):
            return Decimales(my.suma(self.z,other.z))
    def __sub__(self,other):
        if isinstance(other,(int,float)):
            other = my.numtup(other)
            return Decimales(my.resta1(self.z,other))
        if isinstance(other,Decimales):
            return Decimales(my.resta1(self.z,other.z))
    def __mul__(self,other):
        if isinstance(other,(int,float)):
            other = my.numtup(other)
            return Decimales(my.multiplicacion1(self.z,other))
        if isinstance(other,Decimales):
            return Decimales(my.multiplicacion1(self.z,other.z))
    def __truediv__(self,other):
        if isinstance (other,Decimales):
            return Decimales(my.division(self.z,other.z))
        elif isinstance (other ,( int , float )):
            return Decimales(my.division(self.z,my.numtup(other)))
    def __radd__(self,other):
        if isinstance(other,(int,float)):
            other = my.numtup(other)
            return Decimales(my.suma(other,self.z))
        if isinstance(other,Decimales):
            return Decimales(my.suma(other,self.z))
    def __rsub__(self,other):
        if isinstance(other,(int,float)):
            other = my.numtup(other)
            return Decimales(my.resta1(other,self.z))
        if isinstance(other,Decimales):
            return Decimales(my.resta1(other,self.z))
    def __rmul__(self,other):
        if isinstance(other,(int,float)):
            other = my.numtup(other)
            return Decimales(my.multiplicacion1(other,self.z))
        if isinstance(other,Decimales):
            return Decimales(my.multiplicacion1(other,self.z))
    def __rtruediv__(self,other):
        other = Decimales(other)
        return other/self
		
    def __str__(self):
        return my.imprimir(self.z)
    def __repr__(self):
        return my.imprimir(self.z)
    def __eq__(self,other):
        if type(other) != tuple:
            other = my.numtup(other)
        return my.comparacion(self.z,other)
    def __ne__(self,other):
        if my.comparacion(self.z,other)==False:
            pass
if __name__=="__main__":
    pi=Decimales(0)
    for k in range(0,100000000):
        if k%2==0:
            pi = pi + 1/(Decimales(2*k+1))
        else:
            pi = pi - 1/(Decimales(2*k+1))
    pi = pi*4
    for j in range(30,len(pi.z[1])):
        pi.z[1].pop(-1)
    print(pi)
"""pi=Decimales(0)
for k in range(0,100000000):
    if k%2==0:
        pi = pi + 1/(Decimales(2*k+1))
    else:
        pi = pi - 1/(Decimales(2*k+1))
pi = pi*4
for j in range(30,len(pi.z[1])):
    pi.z[1].pop(-1)
print(pi)"""
    
