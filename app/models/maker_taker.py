def predict_role(price):
    import random
    return "Maker" if random.random() > 0.5 else "Taker"
