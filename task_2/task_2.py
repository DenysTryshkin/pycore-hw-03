import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    if min >= 1 and max <= 1000 and (max - min + 1) >= quantity:
        return sorted(random.sample(range(min, max + 1), quantity))
    else:
        return []

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
