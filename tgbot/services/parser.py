

def calcuate(mid_price, quality, price_now, how_much):
    all_price_now = mid_price * quality
    new_mid_price = ((price_now * how_much) + all_price_now) / (how_much + quality)
    return round(all_price_now), round(new_mid_price)

def inspect(msg):
    return msg.isdigit()
