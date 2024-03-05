
p50 = 0.13  # for amount $50 and lower
p50_to_1000 = 0.05  # for $50.01-$1000
p1000 = 0.02  # for $1000.01 and higher
fee = 0.50

sell_price = 100

fee = fee + (50 * p50) + ((sell_price - 50) * p50_to_1000)

print(fee)