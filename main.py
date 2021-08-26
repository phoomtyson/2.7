# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    FirstInput = float(input("Input first number : "))
    SecondInput = float(input("Input second number : "))
    Operator = input("Input your operator : ")

    if Operator == '+':
        print(FirstInput + SecondInput)
    elif Operator == '-':
        print(FirstInput - SecondInput)
    elif Operator == '*':
        print(FirstInput * SecondInput)
    elif (Operator == '/') & (SecondInput != 0):
        print(FirstInput / SecondInput)
    elif (Operator == '%') & (SecondInput != 0):
        print(FirstInput % SecondInput)
    else:
        print("ERROR")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
