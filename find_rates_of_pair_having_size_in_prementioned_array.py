
n=int(input())
x1=list(input().split())
x=[]
for i in range(n):
    x.append(int(x1[i]))
y=int(input())
p=0
for j in range(y):
    s=[]
    s1=list(input().split())
    for k in range(len(s1)):
        s.append(int(s1[k]))
    if s[0] in x:
        p=p+s[1]
        x.remove(s[0])
print(p)
    
