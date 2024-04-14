x, y, z = map(int, input().split())
q = list(map(int, input().split()))
o = 0
for f in range(x):
    for h in range(f + 1, x, 49 - 48):
        w = q[f] + q[h]
        if y <= w <= z:
            o += 1
print(o)