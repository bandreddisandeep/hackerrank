a=[1,3,5]
b=[1,3,5]
c=[]
for i in range(3):
    for j in range(3):
        s=[]
        s.append(a[i])
        s.append(b[j])
        c.append(s)
print(c)
def dif(x,y):
    p=[]
    while(x>0):
        n=x%2
        p.append(str(n))
        x=x//2
    c=''.join(p)
    x=[]
    while(y>0):
        l=y%2
        x.append(str(l))
        y=y//2
    d=''.join(x)
    if(len(c)==len(d)):
        er=0
        for u in range(len(c)):
            if c[u]!=d[u]:
                er=er+1
        return(er)
    elif(len(c)<len(d)):
        er=0
        for i in range(1,len(d)+1):
            if i<len(c)+1:
                if d[-i]!=c[-i]:
                    er=er+1
            elif(d[-i]!='0'):
                er=er+1
        return(er)
    elif(len(c)>len(d)):
        er=0
        for i in range(1,len(c)+1):
            if i<len(d)+1:
                if c[-i]!=d[-i]:
                    er=er+1
            elif(c[-i]!='0'):
                er=er+1
        return(er)
j=0
for i in range(len(c)):
    a=c[i][0]
    b=c[i][1]
    l=dif(a,b)
    j=j+l
print(j)
