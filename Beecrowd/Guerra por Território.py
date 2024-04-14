x=int(input())
y=list(map(int,input().split()))
h=sum(y)/2
e=0
c=0
while e!=h:
    c+=1
    e+=y[0]
    y.pop(0)
print(c)
