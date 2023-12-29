def temperature_modeling(a, b, c, time):
    temperature = a * time**2 + b * time + c
    return temperature

def get_user_input():
    try:
        a = float(input("Enter coefficient a: "))
        b = float(input("Enter coefficient b: "))
        c = float(input("Enter coefficient c: "))
        time = float(input("Enter time in hours: "))
        return a, b, c, time
    except ValueError:
        print("Invalid input. Please enter numeric coefficients and time.")
        return get_user_input()

def read_coefficients_from_file(filename='weather.txt'):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            a, b, c, time = map(float, lines[0].split())
        return a, b, c, time
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found. Make sure the file exists.")
        return None
    except ValueError:
        print(f"Error: File '{filename}' contains invalid numeric values.")
        return None

if _name_ == "_main_":
    print("Step 1: Hard-coded Variables for Weather Modeling")
    a_hardcoded, b_hardcoded, c_hardcoded = 0.1, 2, 10
    time_hardcoded = 5  
    print("Temperature for hardcoded coefficients at time", time_hardcoded, "hours:", temperature_modeling(a_hardcoded, b_hardcoded, c_hardcoded, time_hardcoded))
    print("\n")

    print("Step 2: Keyboard Input for Weather Modeling")
    a_keyboard, b_keyboard, c_keyboard, time_keyboard = get_user_input()
    print("Temperature for keyboard input coefficients at time", time_keyboard, "hours:", temperature_modeling(a_keyboard, b_keyboard, c_keyboard, time_keyboard))
    print("\n")

    print("Step 3: Read from a File for Weather Modeling")
    file_coefficients = read_coefficients_from_file()
    if file_coefficients is not None:
        a_file, b_file, c_file, time_file = file_coefficients
        print("Temperature for file input coefficients at time", time_file, "hours:", temperature_modeling(a_file, b_file, c_file, time_file))
        print("\n")
