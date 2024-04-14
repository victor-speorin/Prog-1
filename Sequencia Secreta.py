n=int(input())
s=0
k=0
for i in range(n):
    x=int(input())
    if x!=s:
        s=x
        k+=1
print(k)