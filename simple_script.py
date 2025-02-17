import datetime

def write_message():
    message = f"Hello, GitHub Actions! Timestamp: {datetime.datetime.now()}"
    print(message)
    with open("output.txt", "w") as file:
        file.write(message)

def add_numbers(a, b):
    return a + b

def multiply_numbers(a, b):
    return a * b

def subtract_numbers(a, b):
    return a - b

if __name__ == "__main__":
    write_message()
    print(f"Sum of 3 and 5: {add_numbers(3, 5)}")
    print(f"Product of 3 and 5: {multiply_numbers(3, 5)}")
    print(f"Difference of 10 and 5: {subtract_numbers(10, 5)}")
    print("nou")