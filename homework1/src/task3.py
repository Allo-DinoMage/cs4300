def check_number(input):
    #Check if number is positive, negative, or zero
    if input > 0:
        print("positive")
    elif input < 0:
        print("negative")
    else:
        print("zero")


def first_10_primes():
    #Print the first 10 prime numbers
    primes = []
    N = 2
    
    #loop that counts up till we get 10 primes
    while len(primes) < 10:
        is_prime = True
        #check if N is divisible by any number from 2 to n-1
        for i in range(2, N):
            if N % i == 0:
                is_prime = False
                break
        
        if is_prime:
            primes.append(N)
            print(N)
        
        N += 1


def sum_1_to_100():
    #Calculate sum of numbers 1 to 100
    j = 1
    sum = 0
    
    while j < 101:
        sum += j
        j += 1
    
    print(f"Sum: {sum}")


if __name__ == "__main__":
    print("Testing check_number:")
    check_number(5)
    check_number(-3)
    check_number(0)
    
    print("\nFirst 10 primes:")
    first_10_primes()
    
    print("\nSum 1 to 100:")
    sum_1_to_100()