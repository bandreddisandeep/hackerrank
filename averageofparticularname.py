q=int(input())
m=[]
for i in range(q):
    x=[]
    x=input().split()
    m.append(x)
y=input()
z=[]
for i in range(len(m)):
    if m[i][0]==y:
        z.append(float(m[i][1]))
        z.append(float(m[i][2]))
        z.append(float(m[i][3]))
d=0
for i in range(len(z)):
    d=d+z[i]
l=d/len(z)
print("%.2f" %l)    
