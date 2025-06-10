import statistics

def calculator():
    count = int(input("How many numbers do you have? "))

    numbers = []
    for i in range(count):
        num = float(input(f"Enter number {i+1}: "))
        numbers.append(num)

    print("What do you want to calculate?")
    print("1. Mean")
    print("2. Median")
    print("3. Mode")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        print("Mean is:", statistics.mean(numbers))
    elif choice == "2":
        print("Median is:", statistics.median(numbers))
    elif choice == "3":
        try:
            print("Mode is:", statistics.mode(numbers))
        except statistics.StatisticsError:
            print("No unique mode found.")
    else:
        print("Invalid choice!")

calculator()
