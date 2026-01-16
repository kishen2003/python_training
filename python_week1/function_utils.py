def greet(name="Guest"):
    return "Hello "+name

def calculate_average(numbers):
    if len(numbers) == 0: return None
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)

def count_evens(numbers):
    count = 0
    for n in numbers:
        if n % 2 == 0:
            count += 1
    return count

def format_message(user, message="completed"):
    return user+" has "+message

if __name__ == "__main__":
    print(greet())
    print(greet("Kishen"))

    print(calculate_average([10, 20, 30]))
    print(calculate_average([]))

    print(count_evens([1, 2, 3, 4, 5, 6]))

    print(format_message("admin"))
    print(format_message("user", "logged in"))
