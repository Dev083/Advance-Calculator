def welcome():
    print('''
Welcome to Calculator
''')

def calculate():
    try:
        # Prompt for user input
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))

        # Prompt for user operation
        operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
% for modulus
** for power
lcm for least common multiple
hcf for highest common factor
qrt for square root
''' )

        if operation == '+':
            print("Sum: {} + {} = {}".format(a,b,a+b))
        elif operation == '-':
            print("Difference: {} - {} = {}".format(a,b,a-b))
        elif operation == '*':
            print("Product: {} * {} = {}".format(a,b,a*b))
        elif operation == '/':
            if b != 0:
                print("Quotient: {} / {} = {}".format(a,b,a/b))
            else:
                print("Error: Division by zero is not allowed.")
        elif operation == '%':
            print("Modulus: {} % {} = {}".format(a,b,a%b))
        elif operation == '**':
            print("Power: {}^{} = {}".format(a,b,a**b))
        elif operation == 'lcm':
            print("LCM: {} and {} = {}".format(a,b,lcm(a,b)))
        elif operation == 'hcf':
            print("HCF: {} and {} = {}".format(a,b,hcf(a,b)))
        elif operation == 'qrt':
            if a >= 0:
                print("Square root: {} = {}".format(a,sqrt(a)))
            else:
                print("Error: Square root of negative number is not defined.")
        else:
            print("Error: Invalid operation.")

    except Exception as e:
        print("Error: {}".format(e))

def lcm(x, y):
    return abs(x*y) // hcf(x,y)

def hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf

def sqrt(n):
    if n < 0:
        return None
    elif n == 0 or n == 1:
        return n
    else:
        sqrt = 0.5 * (n + (1/n))
        while(abs(sqrt*sqrt - n) >= 0.00001):
            sqrt = 0.5 * (sqrt + (n/sqrt))
        return sqrt

# Define again() function to ask user if they want to use the calculator again
def again():

    # Take input from user
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    # If user types Y, run the calculate() function
    if calc_again.upper() == 'Y':
        calculate()

    # If user types N, say goodbye
    elif calc_again.upper() == 'N':
        print('See you later.')

    # If user types anything else, ask again
    else:
        again()

# Call functions
welcome()
calculate()
again()