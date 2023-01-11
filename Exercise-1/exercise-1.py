def multi_sum(num1, num2):
    if(num1*num2 <= 1000):
        print(f"The result(product) is {num1*num2}")

    else:
        print(f"The result(sum) is {num1+num2}.")

number1 = int(input("Enter a number: "))
number2 = int(input("Enter a number: "))

multi_sum(number1, number2) # Function calling
