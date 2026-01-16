def classify_number(n):
    if n>0:
        return "Positive"
    if n==0:
        return "Zero"
    return "Negative"

def sum_of_evens(numbers):
    sum = 0
    for x in numbers:
        if x%2 == 0:
            sum += x
    return sum

def password_check(correct_password):
    attempts = ["1234", "admin", "pass", correct_password]
    i = 0
    while i < len(attempts):
        if attempts[i]==correct_password:
            return "Access Granted"
        i+=1

def filter_positive(numbers):
    lst = list()
    for x in numbers:
        if x<0:
            continue
        lst.append(x)
    return lst

def countdown(n):
    while n>0:
        print(n)
        n-=1

if __name__ == "__main__":
    print("=== Task 1 ===")
    print(classify_number(10))
    print(classify_number(-7))
    print(classify_number(0))

    print("\n=== Task 2 ===")
    print(sum_of_evens([1, 2, 3, 4, 5, 6]))

    print("\n=== Task 3 ===")
    print(password_check("secret"))

    print("\n=== Task 4 ===")
    print(filter_positive([-3, 4, -1, 5, 0]))

    print("\n=== Task 5 ===")
    countdown(5)


