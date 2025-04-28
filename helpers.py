def input_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Enter a positive integer.")
        except ValueError:
            print("Invalid input. Enter an integer.")
