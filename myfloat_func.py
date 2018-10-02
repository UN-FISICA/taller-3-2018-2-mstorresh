
def imprimir(x):
    B , C =x[0]+["."]+x[1] , ""
    for i in range(len(B)):
        C += str(B[i])
    #print(C)
    return (C)
	
def rellenar(a,b): #rellena para que las tuplas sean de la misma longitud
	if len(a[1])>len(b[1]):
		for i in range(len(a[1])-len(b[1])):
			b[1].append(0)
	elif len(b[1])>len(a[1]):
		for i in range(len(b[1])-len(a[1])):
			a[1].append(0)
	if len(a[0])>len(b[0]):
		for i in range(len(a[0])-len(b[0])):
			b[0].insert(1,0)
	elif len(b[0])>len(a[0]):
		for i in range(len(b[0])-len(a[0])):
			a[0].insert(1,0)
def quitceros(a): #quita los ceros
    for j in range(len(a)):
        if a[0]==0:
            a.pop(0)    
    return(a)
def intlist(n): #transforma un entero en una lista
    l = []
    while n != 0:
        l = [n % 10] + l
        n = n // 10
    return (l)
def tupstr(x): #transforma de tupla a string
    rellenar(a,b)
    B , C =x[0]+["."]+x[1] , ""
    for i in range(1,len(B)):
        C += str(B[i])
    return C
def tupint(x): #transforma de tupla a entero
    rellenar(a,b)
    B , C =x[0]+x[1] , ""
    for i in range(1,len(B)):
        C += str(B[i])
    h = int(C)
    return h 
def tupint1(x):
    B,C=x[0]+x[1], ""
    for i in range(1,len(B)):
        C += str(B[i])
    h = int(C)
    return h
def tupflo(x): #transforma de tupla a float
    D , E =x[0]+["."]+x[1] , ""
    for i in range(len(D)):
        E += str(D[i])
    p = float(E)
    return p
def lisint(x): #transforma de una lista a un entero
    B=""
    for i in range(len(x)):
        B +=str(x[i])
    return int(B)

def numtup(x): #transforma de un float o entero a una tupla
    c=1
    if x<0:
        x=-1*x
        c=0
    else:
        x=x
    if type(x)==float:
        t1=list(map(int,str(int(x))))
        t2=list(map(int,str(x).split(".")[1]))
    if type(x)==int:
        t1=list(map(int,str(x)))
        t2=[0]
    if c==0:
        t1.insert(0,"-")
    else:
        t1.insert(0,"+")
    return(t1,t2)
#Desde esta parte es la forma de operar con las tuplas transformandolas a entero            
def suma1(a,b):
    rellenar(a,b)
    B , C =a[0]+a[1] , ""
    for i in range(1,len(B)):
        C += str(B[i])
    c = int(C)
    E , D =b[0]+b[1] , ""
    for i in range(1,len(E)):
        D += str(E[i])
    e = int(D)
    s = c+e
    n = ([],[])
    l=intlist(s)
    for k in range(len(l)-1,len(a[0])-2,-1):
        n[1].insert(0,l[k]) 
    l.reverse()
    for i in range(len(l)-1,len(a[1])-1,-1):
        n[0].insert(0,l[i])
    n[0].reverse()
    n[0].insert(0,a[0][0])   
    #print(n)
    return n
def resta1(a,b):
    rellenar(a,b)
    B , C =a[0]+a[1] , ""
    for i in range(1,len(B)):
        C += str(B[i])
    c = int(C)
    E , D =b[0]+b[1] , ""
    for i in range(1,len(E)):
        D += str(E[i])
    e = int(D)
    s = c-e
    if c>e:
        n=([],[])
        l=intlist(s)
        for k in range(len(l)-1,len(a[0])-2,-1):
            n[1].insert(0,l[k]) 
        l.reverse()
        for i in range(len(l)-1,len(a[1])-1,-1):
            n[0].insert(0,l[i])
        n[0].reverse()
        n[0].insert(0,"+")
        #print(n)
        return n
    if c<e:
        s=s*(-1)
        n=([],[])
        l=intlist(s)
        for k in range(len(l)-1,len(a[0])-2,-1):
            n[1].insert(0,l[k]) 
        l.reverse()
        for i in range(len(l)-1,len(a[1])-1,-1):
            n[0].insert(0,l[i])
        n[0].reverse()
        n[0].insert(0,"-")  
        #print(n)
        return n

def multiplicacion1(a,b):
    a0=len(a[0])
    a1=len(a[1])
    b0=len(b[0])
    b1=len(b[1])
    c=tupint1(a)
    e=tupint1(b)
    s = c*e
    if a[0][0]==b[0][0]:
        n=([],[])
        l=intlist(s)
        #print(l)
        for k in range(len(l)-1,(len(l)-(a1+b1))-1,-1):
            n[1].insert(0,l[k])
        l.reverse()
        for i in range(len(l)-1,(a1+b1)-1,-1):
            n[0].insert(0,l[i])
        n[0].reverse()
        n[0].insert(0,"+")
        #print(s)    
        #print(n)
        return n
    if a[0][0]!=b[0][0]:
        if c<0:
            c = c*(-1)
        if e<0:
            e = e*(-1)
        n=([],[])
        l=intlist(s)
        #print(l)
        for k in range(len(l)-1,(len(l)-(a1+b1))-1,-1):
            n[1].insert(0,l[k])
        l.reverse()
        for i in range(len(l)-1,(a1+b1),-1):
            n[0].insert(0,l[i])
        n[0].reverse()
        n[0].insert(0,"-")
        #print(s)    
        #print(n)
        return n
def division1(a,b):
    c=tupint(a)
    e=tupint(b)
    s = c/e
    if a[0][0]==b[0][0]:
        n=([],[])
        S=str(s)
        l1=list(S[0:S.find(".")])
        l2=list(S[S.find(".")+1:])
        if a[1][-1] == 0 or b[1][-1]==0:
            if l2[-1]==0:
                l2.pop(-1)
        for k in range(len(l2)-1,-1,-1):
            n[1].insert(0,int(l2[k]))
        l1.reverse()
        for i in range(len(l1)-1,-1,-1):
            n[0].insert(0,int(l1[i]))
        n[0].reverse()
        n[0].insert(0,"+")   
        #print(n)
        return n
    if a[0][0]!=b[0][0]:
        if c<0:
            c = c*(-1)
        if e<0:
            e = e*(-1)
        n=([],[])
        S=str(s)
        l1=list(S[0:S.find(".")])
        l2=list(S[S.find(".")+1:])
        if a[1][-1] == 0 or b[1][-1]==0:
            if l2[-1]==0:
                l2.pop(-1)
        for k in range(len(l2)-1,-1,-1):
            n[1].insert(0,int(l2[k]))
        l1.reverse()
        for i in range(len(l1)-1,-1,-1):
            n[0].insert(0,int(l1[i]))
        n[0].reverse()
        n[0].insert(0,"-")  
        #print(n)
        return n
#Desde esta parte es la forma de operar con la tuplas sin transformarlo a entero
def suma(a,b):	
    rellenar(a,b)
    a[0].insert(1,0)
    b[0].insert(1,0)
    c=([],[])
    c[1].append((a[1][-1]+b[1][-1])%10)
    for i in range(len(a[1])-1,0,-1): 
        c[1].insert(0,((a[1][i-1]+b[1][i-1])%10 +(a[1][i]+b[1][i])//10)%10)
    c[0].append(((a[0][-1]+b[0][-1])%10 + (a[1][0]+b[1][0])//10)%10)
    for j in range(len(a[0])-1,1,-1):
        c[0].insert(0,((a[0][j-1]+b[0][j-1])%10 +(a[0][j]+b[0][j])//10)%10)	
    c[0].insert(0,a[0][0])
    if c[0][1] ==0:
        c[0].pop(1)
    #print (c)
    return c	
def division(a,b,n=100):
    c=max(len(b[1]),len(a[1]))
    for i in range(c-len(a[1])):
        a[1].append(0)
    for j in range(c-len(b[1])):
        b[1].append(0)
    a1=a[0][:]    
    a1.pop(0)
    a1.extend(a[1])
    b1=b[0][:]
    b1.pop(0)
    b1.extend(b[1])
    quitceros(a1)
    quitceros(b1)
    a1=lisint(a1)
    b1=lisint(b1)
    l1= list(map(int, str(a1//b1)))
    l2=[]
    res=a1%b1    
    for k in range(n):
        div=res*10
        prod=div//b1*b1
        l2.append(div//b1)
        res=div-prod
    F=(l1,l2)
    if a[0][0]==b[0][0]:
        F[0].insert(0,'+')
    else:
        F[0].insert(0,'-')          
    #print(F)  
    return F
def comparacion(a,b):
    rellenar(a,b)
    c=1
    for i in range(len(a[0])):
        if a[0][i] != b[0][i]:
            c=0
    for j in range(0,len(a[1])):
        if a[1][j] != b[1][j]:
            c=0
    if c==1:
        #print("son iguales")
        return a==b
    if c==0:
        #print("No son iguales")
        return False
#comparacion(a,b)
"""if __name__ =="__main__":
    a=(["+",7,5],[1,2,3])
    b=(["+",5],[1,2])
    
    c=suma(a,b)
    d=resta1(a,b)
    e=multiplicacion1(a,b)
    f=division(a,b)
    g=comparacion(a,b)
    print(c)
    print(d)
    print(e)
    print(f)
"""