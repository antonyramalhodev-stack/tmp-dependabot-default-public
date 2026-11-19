RATE = 0.2
MAX_ITEMS = 50


def total(items):
    result = 0
    for item in items:
        result += item["price"] * item["qty"]
    return result


def average(items):
    return total(items) / len(items)


def apply_discount(amount, rate=RATE):
    return amount - amount * rate
