import myfloat_func as my
class Decimales:
    def __init__(self, z): #parametro son las tuplas, enteros y decimales
        self.z=z
        if (type(z) is int) or (type(z) is float):
            self.z=my.numtup(z)
        else:
            self.z=z
    def __add__(self,other):
        if isinstance(other,(int,float)):
            other = my.numtup(other)
            return Decimales(my.suma(self.z,other))
        if isinstance(other, Decimales):
            return Decimales(my.suma(self.z,other))
    def __sub__(self,other):
        if isinstance(other,(int,float)):
            other = my.numtup(other)
            return Decimales(my.resta1(self.z,other))
        if isinstance(other,Decimales):
            return Decimales(my.resta1(self.z,other))
    def __mul__(self,other):
        if isinstance(other,(int,float)):
            other = my.numtup(other)
            return Decimales(my.multiplicacion1(self.z,other))
        if isinstance(other,Decimales):
            return Decimales(my.multiplicacion1(self.z,other))
    def __truediv__(self,other):
        if isinstance(other,(int,float)):
            other = my.numtup(other)
            return Decimales(my.division(self.z,other))
        if isinstance(other,Decimales):
            return Decimales(my.division(self.z,other))
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
        if isinstance(other,(int,float)):
            other = my.numtup(other)
            return Decimales(my.division(other,self.z))
        if isinstance(other,Decimales):
            return Decimales(my.division(other,self.z))
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
if __name__=="main":
    pi=Decimales(0)
    for k in range(0,30000):
        pi = pi + ((-1)**k)/(Decimales(2*k+1))
    pi *= 4
    print(pi)
