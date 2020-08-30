# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# imports
import math
import random


def opChoice(choice, arr):
    if choice == 1:
        arr.sort()
        print("Array numbers sorted in ascending order is: " + str(arr))

    elif choice == 2:
        arr.sort(reverse=True)
        print("Array numbers sorted in descending order is: " + str(arr))

    elif choice == 3:
        print("Sum of all numbers in the array is: " + str(sumArray(arr)))

    elif choice == 4:
        print("Product of all numbers in the array is: " + str(productArray(arr)))

    elif choice == 5:
        print("Average value of all the array numbers is: " + str(sumArray(arr) / len(arr)))

    elif choice == 6:
        print("New array after all its numbers were squared: " + str(squareArray(arr)))

    elif choice == 7:
        print("New array after all its numbers were square rooted: " + str(sqrtArray(arr)))

    elif choice == 8:
        even = evenOdd(arr)[0]
        odd = evenOdd(arr)[1]
        print("The number of even versus odd numbers in the array:"
              "\nEvens: " + str(even) + "   Odds: " + str(odd))

    elif choice == 9:
        print(str(len(primeCount(arr))) + " Prime numbers were found in the array:\n" + str(primeCount(arr)))

    elif choice == 10:
        base = input("What base would you like to convert the array numbers to? (2 - 32): ")
        print("The array converted into base " + base + " is:\n" + str(baseConvertArray(arr, base)))

    else:
        retry = input("\nPlease choose an operation listed above by entering a number 1-10: ")
        opChoice(int(retry), arr)


def initArray(n, low, high):
    arr = []
    for i in range(n):
        arr.append(random.randint(low, high))
    return arr


def sumArray(arr):
    total = 0
    for i in range(len(arr)):
        total += int(arr[i])
    return total


def productArray(arr):
    total = 1
    for i in range(len(arr)):
        total *= int(arr[i])
    return total


def squareArray(arr):
    sqrArr = []
    for i in range(len(arr)):
        sqrArr.append(pow(arr[i], 2))
    return sqrArr


def sqrtArray(arr):
    sqrtArr = []
    for i in range(len(arr)):
        sqrtArr.append(math.sqrt(arr[i]))
    return sqrtArr


def evenOdd(arr):
    evenCount = 0
    oddCount = 0
    for i in range(len(arr)):
        if arr[i] % 2 == 0 or arr[i] == 0:
            evenCount += 1
        else:
            oddCount += 1
    return evenCount, oddCount


def isPrime(x):
    divisor = 2
    while divisor < x:
        if x % divisor != 0:
            divisor += 1
        else:
            return False
    return True


def primeCount(arr):
    primes = []
    for i in range(len(arr)):
        if isPrime(arr[i]):
            primes.append(arr[i])

    return primes


def baseConverter(x, b):
    newNum = []
    quo = 1

    while quo != 0:
        quo = x // b
        rem = x % b

        if rem > 9:
            newNum.append(chr(rem + 87))
        else:
            newNum.append(rem)
        x = quo

    newNum.reverse()
    return newNum


def baseConvertArray(arr, b):
    baseArr = []

    for i in range(len(arr)):
        snip = ""
        for s in baseConverter(int(arr[i]), int(b)):
            snip += str(s)
        baseArr.append(snip)

    return baseArr


print("This program will generate a random array based on parameters you choose.")
size = int(input("Enter array size: "))
minimum = int(input("Enter lowest possible value for the array: "))
maximum = int(input("Enter highest possible value for the array: "))
op = input("\nAvailable operations for array:"
           "\n1. Sort array in ascending order"
           "\n2. Sort array in descending order"
           "\n3. Sum all numbers in array"
           "\n4. Calculate product of all numbers in array"
           "\n5. Calculate the average of all numbers in array"
           "\n6. Square each individual number in array"
           "\n7. Calculate square root of each individual number in array"
           "\n8. Determine the amount of even numbers versus odd numbers"
           "\n9. Identify the prime numbers in the array"
           "\n10. Convert the numbers in the array from base 10 to a different base "
           "\nEnter the number of the operation you want to perform on the array: ")

array = initArray(size, minimum, maximum)

print("Array size: " + str(size) + "\nOperation choice: " + op)
print("\nRandom Array: " + str(array))

opChoice(int(op), array)
