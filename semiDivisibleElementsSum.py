n=list(input().split())
a=int(n[0])
b=int(n[1])

x=[]
y=[]
for i in range(1,b+1//2):
    flag=0
    for j in range(2,i):
        if i%j==0:
            flag=1
    if flag==0:
        x.append(i)
    
for k in range(1,b//2):
    y.append(k**2)


z=0
for i in range(a,b+1):
    j=0
    while i>x[j]**2:
        j=j+1
    #print(i)
    #print("and")
    #print(x[j-1])
    #print(x[j])
    if (i%x[j-1]==0 and i%x[j]!=0) or (i%x[j-1]!=0 and i%x[j]==0):
        if i not in y:
            z=z+i
print(z)           
