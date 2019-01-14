# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 12:45:19 2019

@author: sounak
"""
from PIL import Image
def hashed(n):
    return n%256
def digest(img,n1,n2,cp,x,y):
    pixel_map=img.load()
    if(n1%x!=0 and n2%y!=0):
        m1=n1+x-(n1%x)
        m2=n2+y-(n2%y)
    else:
        m1=n1
        m2=n2
    import crt
    x1=x
    x2=y
    l=0
    j,k,k1,k2=0,0,0,0
    ar=[0 for i in range((x*y))]
    t=[]
    while x2<m2:
        x1=x
        while x1<m1:
            
            while k2<x2:
                while k1<x1:
                    ar[l]=img[k1][k2]
                    l+=1
                    k1+=1
                    k2+=1
                k1=k1-x1
            k1=x1
            k2=k2-x2
            b=crt.findx((x*y),ar,cp)
            t[j][k]=b
            j+=1
            k+=1
            x1+=x
        x1=x
        x2+=y
        k1=0
        k2+=y
        l=0
    h=map(hashed,t)
    for i in t:
        for j in i:
            t[i][j]=hashed(t[i][j])
            
            