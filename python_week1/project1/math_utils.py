def calculate_sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total

def calculate_average(numbers):
    if len(numbers) == 0:
        return None
    total = calculate_sum(numbers)
    return total / len(numbers)
