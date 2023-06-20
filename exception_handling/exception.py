# try:
#     # Code block that may raise an exception
#     # ...
# except ExceptionType1:
#     # Handler for ExceptionType1
#     # ...
# except ExceptionType2:
#     # Handler for ExceptionType2
#     # ...
# else:
#     # Executed if no exception occurs
#     # ...
# finally:
#     # Executed regardless of whether an exception occurred or not
#     # ...
# try:
#     num1 = int(input("Enter a number: "))
#     num2 = int(input("Enter another number: "))
#
#     result = num1 / num2
#     print("Result:", result)
#
# except ValueError:
#     print("Invalid input. Please enter a valid number.")
#
# except ZeroDivisionError:
#     print("Cannot divide by zero.")
#
# else:
#     print("Division operation successful.")
#
# finally:
#     print("End of program.")
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

# Check if inputs are valid numbers
if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)

    # Check if the second number is not zero
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Cannot divide by zero.")
else:
    print("Invalid input. Please enter valid numbers.")
