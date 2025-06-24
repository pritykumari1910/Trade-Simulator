def calculate_market_impact(quantity):
    k = 0.01  # market impact coefficient
    return k * (quantity ** 0.5)
