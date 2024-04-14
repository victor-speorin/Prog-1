N = int(input())
min_price_per_gram = float("inf")
for _ in range(N):
    P, G = map(float, input().split())
    price_per_gram = P / G
    min_price_per_gram = min(min_price_per_gram, price_per_gram)
total_price = min_price_per_gram * 1000
print(f'{total_price:.2f}')