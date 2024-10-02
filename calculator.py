import time

def calculator():
    print("Hello!")
    time.sleep(2)

calculator()

while True:
    try:
        first_num = int(input("What is your first number? "))
        second_num = int(input("What is your second number? "))

    except ValueError:
        print("That's not an integer.")
        time.sleep(1)
        continue

    print(f"Your numbers are: {first_num} and {second_num}.")

    time.sleep(1)

    operation = input("What is your operation? \n"
                      "a. Multiplication \n"
                      "b. Division \n"
                      "c. Addition \n"
                      "b. Subtraction \n")

    time.sleep(1)
    if operation == "a":
        result = first_num * second_num
        print(f"Your result is {result}")
        continue

    elif operation == "b":
        result = round(first_num / second_num, 2)
        print(f"Your result is ~{result}")
        continue

    elif operation == "c":
        result = first_num + second_num
        print(f"Your result is {result}")
        continue

    elif operation == "d":
        result = first_num - second_num
        print(f"Your result is {result}")
        continue

    else:
        print("Please chose the letter of the operation! ")
        calculator()

calculator()