
m,n = input().split()
x=[]
y=[]
for i in range (int(m)):
    a=input()
    x.append(a)
    
for j in range(int(n)):
    b=input()
    y.append(b)

z=[]

for k in range(len(x)):
    if x[k] not in z:
        z.append(x[k])
for l in range(len(y)):
    if y[l] not in z:
        z.append(y[l])

for t in range(len(z)):
    if z[t] in x:
        s=[]
        for o in range(len(x)):
            if z[t]==x[o]:
                s.append(int(o))
        for l in range(len(s)-1):
            print(s[l]+1,end=" ")
        print(s[-1]+1)

    else:
        print(-1)




