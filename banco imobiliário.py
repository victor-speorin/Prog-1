y,x=map(int,input().split())
yd=y
yf=y
ye=y
for i in range(x):
    l=list(map(str,(input().split())))
    if l[0]=='V':
        b=int(l[2])
        if l[1]=='D':
            yd+=b
        elif l[1]=='E':
            ye+=b
        elif l[1]=='F':
            yf+=b
    elif l[0]=='C':
        u=int(l[2])
        if l[1]=='D':
            yd=yd-u
        elif l[1]=='E':
            ye=ye-u
        elif l[1]=='F':
            yf=yf-u
    elif l[0]=='A':
        h=int(l[3])
        if l[1]=='D':
            if l[2]=='E':
                yd+=h
                ye-=h
            if l[2]=='F':
                yd+=h
                yf-=h
        if l[1]=='E':
            if l[2]=='D':
                ye+=h
                yd-=h
            if l[2]=='F':
                ye+=h
                yf-=h
        if l[1]=='F':
            if l[2]=='D':
                yf+=h
                yd-=h
            if l[2]=='E':
                yf+=h
                ye-=h

print(yd,ye,yf)
