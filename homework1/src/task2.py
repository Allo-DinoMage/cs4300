def varsDataTypes():
    #integers:
    numberA = 3
    numberB = 2
    product = numberA*numberB
    print(f"{numberA} times {numberB} equals {product}")

    #floats:
    floatA = 2.2
    floatB = 3.3
    fProduct = floatA*floatB
    print(f"{floatA} times {floatB} equals {fProduct}")

    #here's a string:
    student = "Gary"
    #and here's a boolean
    passed = False


    if passed == False:
        print(f"{student} failed!")

    else:
        print(f"{student} passed!")

if __name__ == "__main__":
    varsDataTypes()
