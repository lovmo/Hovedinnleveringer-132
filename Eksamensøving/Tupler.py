tall=(1,2,3,4,5)
storetall=(99,88,77,66,55)
bokstaver=('a','b','c','d','e')

def tripler(i1,y1,m1):
    ut = []

    for i in range(0, len(i1)):
        ut.append((i1[i], y1[i], m1[i]))
    
    return ut

x = tripler(tall,storetall,bokstaver)

tall=[1,2,3,4]

def iter(liste):
    k = []
    for i in liste:
        for u in liste:
            k.append((i,u))
    return k

kombi = iter(tall)



dager=[(1,'man'),(2,'tir'),(3,'ons'),(4,'tor'),(5,'fre'),\
 (6,'lør'),(7,'søn')]
        
temperaturer=[('man',11),('tir',9),('ons',7),('tor',12),\
 ('fre',11),('lør',9),('søn',8)]

def koble(A,B):
    C=[]
    for (x,y) in A:
        for (v,w) in B:
            if y==v: C.append((x,w))
    return C

h = koble(dager, temperaturer)
print(h)


print()
print()
print()
print()

d = koble(temperaturer, dager)
print(d)
        
