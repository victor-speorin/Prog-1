Xm, Ym, Xr, Yr = map(int, input().split())
if Xm == Xr or Ym == Yr:
    print(abs(Xm - Xr) + abs(Ym - Yr))
else:
    if Xm < Xr:
        dx = Xr - Xm
    else:
        dx = Xm - Xr

    if Ym < Yr:
        dy = Yr - Ym
    else:
        dy = Ym - Yr
    print(dx + dy)