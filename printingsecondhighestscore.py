q=int(input())
m=[]
for i in range(q):
    n=[]
    y=float(input())
    n.append(y)
    x=input()
    n.append(x)
    m.append(n)
print(m)
m.sort()
print(m)
a=min(m)
b=[]
for i in range(len(m)):
    if m[i][0]!=a[0]:
        b.append(m[i])
c=min(b)
for i in range(len(b)):
    if b[i][0]==c[0]:
        print(b[i][1])
        
