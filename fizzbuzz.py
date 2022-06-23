#Divide by 3 = fizz
#Divide by 5 = buzz
#Divide by 3 and 5 = fizzbuzz
#None of the above = print x

while True:

    x = int(input("Enter Number:    "))

    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)