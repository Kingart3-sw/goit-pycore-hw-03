import random
def get_numbers_ticket(min_val: int, max_val: int, quantity: int) -> list:
    if not (1 <= min_val <= max_val <= 1000):
        return []
    if not (1 <= quantity <= (max_val - min_val + 1)):
        return []
    numbers = random.sample(range(min_val, max_val + 1), quantity)
    return sorted(numbers)
print("1:", get_numbers_ticket(1, 49, 6))
print("2:", get_numbers_ticket(1, 36, 5))
print("(min < 1):", get_numbers_ticket(0, 50, 5))
print("(500):", get_numbers_ticket(1, 10, 15))