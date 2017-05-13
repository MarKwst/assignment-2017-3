import argparse
import random
import sys

n = int(sys.argv[1])

D = []

c = n*(n-1)/6

while c>0:
    K = []    
    #metraei poses fores vriskete kathe stixeio mesa sto D sunolo
    for i in D:
        k = D.count(i)
        K.append(k)
        
    K.sort()
    L = set()
    #dimiourgw sunolo L me ta i stoixeia apo to K pou ikanopoioun tu sunthiki((u-1)\2)
    for i in K:
        if i<=((n-1)/2):
            L.add(i)
            
    #kai epilegw tuxaia ena arithmo apo afto to L sunolo
    if L == 0:
        x =  random.choice(L)
    else:
         x =  random.choice(range(1,n+1))

    #dimiourgw ena sunolo me stoixeia apo tois aritmous n
    sunolo = set(range(1,n+1))

    #afairw to x apo afta giati to exoume idi parei
    sunolo.remove(x)

    #epilegw z kai y kai ta fairw apo to sunolo epishs wste na mhn parw katala8os to idio
    z = random.sample(sunolo,1)
    sunolo.remove(z[0])

    y = random.sample(sunolo,1)
    sunolo.remove(y[0])
    pairs = []
    if ((((x,y[0]) and (x,z[0]))and((z[0],x)and (y[0],x))) not in D)and((((x,y[0]) and (x,z[0]))and((z[0],x)and (y[0],x))) not in pairs):
        pairs.append((x,y[0]))
        pairs.append((y[0],x))
        pairs.append((x,z[0]))
        pairs.append((z[0],x))
        w = random.sample(sunolo,1)
        if (y[0],z[0],w[0]) in D:
            D.remove((y[0],z[0],w[0]))
            c = c + 1
        D.append((x,y[0],z[0]))
        c = c - 1

print(D)
print(len(D))
