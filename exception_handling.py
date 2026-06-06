try:
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))
    result = a/b
except ValueError:
    print("thats not a number.")
except ZeroDivisionError:
    print("cannot divide by zero.")     
else:
    print("result is:", result)
finally:
    print("thank you for using the calculator.")          

