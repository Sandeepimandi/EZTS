T = int(input())

for i in range(T):
    N, X = map(int, input().split())
    total_slices = N * X
    total_pizzas = 0
    while total_slices > 0:
        total_slices -= 4
        total_pizzas += 1
    
    print(total_pizzas)