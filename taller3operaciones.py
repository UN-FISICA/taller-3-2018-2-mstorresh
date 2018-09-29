#!/usr/bin/python
# -*- coding: UTF-8 -*-
a=(["+",5,8],[2,3,3,4])
b=(["+",6,3,2],[1,8,3])
def prim(a):
	B , C =a[0]+["."]+a[1] , ""
	for i in range(len(B)):
		C += str(B[i])
	print(C)
	return
"""def suma(a,b):
	B , C =a[0]+["."]+a[1] , ""
	for i in range(1,len(B)):
		C += str(B[i])
	D , E =b[0]+["."]+b[1] , ""
	for i in range(1,len(D)):
		E += str(D[i])
	c = float(C)
	e = float(E)
	s = c+e
	print(s)
	
	return
suma(a,b)"""
def rellenar(a,b):
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
def suma(a,b):	
    rellenar(a,b)
    a[0].insert(1,0)
    b[0].insert(1,0)
    c=([],[])
    c[1].append(a[1][-1]+b[1][-1]%10)
    for i in range(len(a[1])-1,0,-1): 
        c[1].insert(0,((a[1][i-1]+b[1][i-1])%10 +(a[1][i]+b[1][i])//10)%10)
    c[0].append(((a[0][-1]+b[1][-1]%10 + a[1][0]+b[1][-1]//10))%10)
    for j in range(len(a[0])-1,1,-1):
        c[0].insert(0,((a[0][j-1]+b[0][j-1])%10 +(a[0][j]+b[0][j])//10)%10)	
    c[0].insert(0,a[0][0])
    if c[0][1] ==0:
        c[0].pop(1)
    prim (c)
    print (c)
suma(a,b)	
def resta(a,b):
    if a[0][0] =="+" and b[0][0]=="-":
        