def fun(x):
    if x=='print':
        print(l)
    elif x=='reverse':
        l.reverse()
    elif x=='sort':
        l.sort()
    elif x=='pop':
        l.remove(l[-1])
    else:
        print('invalid')

def ins(x,y):
    l.insert(x,y)
    
    
def rem(y):
    l.remove(y)
    
def app(y):
    l.append(y)
    
    
n=int(input())
l=[]
for i in range(n):
    x=input().split()
    if x[0]=='insert':
        ins(int(x[1]),int(x[2]))
    elif x[0]=='remove':
        rem(int(x[1]))
    elif x[0]=='append':
        app(int(x[1]))
    else:
        fun(x[0])
    
