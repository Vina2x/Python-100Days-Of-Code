n= int(input("Enter the number you want to check: "))

def prime_checker(number):
    isPrime= True
    for int in range(2, number):
        if number%int==0:
            isPrime=False
    if isPrime:
        print("It's a prime number!")
    else:
        print("It's not a prime number!")


prime_checker(number=n)