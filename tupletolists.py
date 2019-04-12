n=int(input())
x=input().split()
t1=[]
t=()
for i in range(len(x)):
    t1.append(int(x[i]))
t=tuple(t1)
print(hash(t))
    
    
