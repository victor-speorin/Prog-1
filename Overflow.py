x=int(input())
y,z,w=map(str,input().split())
y1=int(y)
w1=int(w)
if z=='+':
    if y1+w1>x:
        print('OVERFLOW')
    else:
        print('OK')
else:
    if y1*w1>x:
        print('OVERFLOW')
    else:
        print('OK')