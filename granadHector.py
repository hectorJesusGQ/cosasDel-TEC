import sys
sys.setrecursionlimit(2500)

#Dominio: List [1<List<10000000000], r[1<=r<=5]
#Codominio:True/False
def OnlyifR(List, r):   #O(n^2)
    for d in List:
        if List.count(d) > r: return False 
    return True

#Dominio: c [1<=c<=20], r [1<=r<=5]
#Codominio: Eficaz(str)
def Central(c, r, ):    #O(n)
    a=1000
    b=1000*c
    Eficaz=str()
    while b <= 99999:
        totalNum, a, b = TheDiv(a, b, c)
        if OnlyifR(totalNum, r): 
            Eficaz+=(str(b) + "/" + str(a) + "=" + str(c) + "\n")
        b+=c
        a+=1
    return Eficaz

#Dominio:a [1000<=a<=99999], b  [1000<=a<=99999],c [1<=c<=20]
#Codominio: totalNum(bStr + aStr)[str 10 digits], a [1000<=a<=99999], b  [1000<=a<=99999]
def TheDiv(a, b, c):    #O(n)
    if b == a * c:
        aStr=str(a).zfill(5)
        bStr=str(b).zfill(5)
        return bStr + aStr, a, b
    if a * c > b: #O(n)
        return TheDiv(a, b + 1, c)
    return TheDiv(a + 1, b, c)

#Dominio:t [1<=t<=100], c [1<=c<=20], r [1<=r<=5]
#Codominio: 
#t*(O(n^2)) or O(t*(n^2))
t=int(input())  
while t:
    t-=1
    c,r=input().split()
    c=int(c)
    r=int(r)
    print((Central(c,r)))
