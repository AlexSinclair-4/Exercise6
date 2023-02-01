numbers = []

while True:
    user_input = input("Enter a number (press enter to stop): ")
    if user_input == '':
        break
    elif user_input.isnumeric():
        numbers.append(int(user_input))
    else:
        print("Invalid input. Please enter a number.")

if len(numbers) == 0:
    print("No numbers were entered.")
else:
    sum_of_numbers = sum(numbers)
    average = sum_of_numbers / len(numbers)

    print(f"Sum of numbers: {sum_of_numbers}")
    print(f"Average: {average}")