

def calcuate(mid_price, quality, price_now, how_much):
    all_price_now = mid_price * quality
    new_mid_price = ((price_now * how_much) + all_price_now) / (how_much + quality)
    return round(all_price_now, 2), round(new_mid_price, 2)

def inspect(msg):
    msg = msg.replace(',','1')
    msg = msg.replace('.', '1')
    return msg.isdigit()

def dot(some_str):
    if ',' in some_str:
        new_some_str = some_str.replace(',','.')
    else:
        new_some_str = some_str
    return new_some_str
