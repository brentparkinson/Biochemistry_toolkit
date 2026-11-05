print ("Dilution Calculator")
def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Value must be greater than zero.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
def calculate_dilution(c1, v2, c2):
    v1 = (c2 * v2) / c1
    d1 = v2 - v1
    return v1, d1
def format_result(value):
    if abs(value) <= 1e-4:
        return f"{value:.2e}"
    else:
        return f"{value:.3g}"
c1 = get_positive_float("Enter stock concentration (M): ")
v2 = get_positive_float("Enter desired final volume (L): ")
while True:
    c2 = get_positive_float("Enter desired concentration (M): ")
    if c2 > c1:
        print("Error: Desired concentration cannot be greater than stock concentration.")
    else:
        break    
v1, d1 = calculate_dilution(c1, v2, c2)
print("\n--- RESULTS ---")
print("Required stock volume (L):", format_result(v1))
print("Required diluent volume (L):", format_result(d1))
print("---------------")