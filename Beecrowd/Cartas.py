x, y, z, k, p = map(int, input().split())
if x < y < z < k < p:
    print("C")
elif x > y > z > k > p:
    print("D")
else:
    print("N")
