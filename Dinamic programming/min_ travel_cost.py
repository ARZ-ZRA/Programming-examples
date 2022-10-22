def count_price(n, price: list):
    """Функция минимальной стоимости передвижения"""
    cost = [None, price[1], price[1]+price[2]]+[0]*(n-2)
    for i in range(3, n+1):
        cost[i] = price[i] + min(cost[i-1], cost[i-2])
    return cost[n]


print(count_price(5, [44, 55, 77.3, 33, 55, 100]))
