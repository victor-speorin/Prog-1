x=int(input())
y=0
for i in range(x):
    l,c=map(int,input().split())
    if l>c:
        y+=c
print(y)