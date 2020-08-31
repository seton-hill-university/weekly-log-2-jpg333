# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# imports
import math
import random

# introductory message
print("This program will generate a random array based on parameters you choose."
      "\nYou then will be able to perform various operations on the array")


# print list of array operations
def opMenu(arr):
    # list of available operations. Record user choice
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

    # calls choice handling method and passes on array and operation choice
    opChoice(arr, int(op))
    return


# function to handle choice of operation
def opChoice(arr, choice):
    # option 1 is a simple ascending sort
    if choice == 1:
        arr.sort()
        print("Array numbers sorted in ascending order is:\n" + str(arr))

    # option 2 is a descending sort
    elif choice == 2:
        arr.sort(reverse=True)
        print("Array numbers sorted in descending order is:\n" + str(arr))

    # option 3 sums all elements using method sumArray()
    elif choice == 3:
        print("Sum of all numbers in the array is: " + str(sumArray(arr)))

    # option 4 calculates product of all elements using method productArray()
    elif choice == 4:
        print("Product of all numbers in the array is: " + str(productArray(arr)))

    # option 5 calculates the mathematical average of all elements using method sumArray()
    #   and then dividing the sum by the array size
    elif choice == 5:
        print("Average value of all the array numbers is: " + str(sumArray(arr) / len(arr)))

    # option 6 returns a new array determined by squaring all elements of the original array using method squareArray()
    elif choice == 6:
        print("New array after all its numbers were squared:\n" + str(squareArray(arr)))

    # option 7 returns a new array determined by taking the square root of all elements of the original array
    #   using method sqrtArray()
    elif choice == 7:
        print("New array after all its numbers were square rooted:\n" + str(sqrtArray(arr)))

    # option 8 counts the number of even and odd numbers in the array by using method evenOdd()
    elif choice == 8:
        # evenOdd() has 2 return values, where [0] is the even number and [1] is the odd
        even = evenOdd(arr)[0]
        odd = evenOdd(arr)[1]
        print("The number of even versus odd numbers in the array:"
              "\nEvens: " + str(even) + "   Odds: " + str(odd))

    # option 9 returns a subset of the original array that contains only prime numbers using method primeCount().
    #   also displays the amount of primes via the length of the primes array
    elif choice == 9:
        print(str(len(primeCount(arr))) + " prime numbers were found in the array:\n" + str(primeCount(arr)))

    # option 10 returns a new array determined by converting all elements in the original array from base 10 to
    #   a different base (2-32) using method baseConvertArray()
    elif choice == 10:
        base = input("Enter the base you would like to convert the array numbers to [2 - 32]: ")
        # error message and retry
        while int(base) < 2 or int(base) > 32:
            base = input("Error: please enter a desired base between 2 and 32 (inclusive): ")

        print("The array converted into base " + base + " is:\n" + str(baseConvertArray(arr, base)))

    # if no valid option is selected, output error message with another prompt for a valid option.
    #   then recursive call to opChoice()
    else:
        print(choice)
        retry = input("\nPlease choose an operation listed above by entering a number 1-10: ")
        opChoice(arr, int(retry))


# driving method from which other functions are chained
def start():

    # initial selection
    print("   Array Type Selection:\n"
          "1. Build your own array\n"
          "2. Generate a random array\n")
    answer = input("Enter '1' or '2': ")

    # decision handling for user input or randomly generated array
    if answer == '1':
        array = byoArray()
    elif answer == '2':
        array = randArray()
    else:
        return 0

    # ask if user is satisfied with the array
    keep = input("Are you satisfied with your array?\n"
                 "(Enter 'y' to proceed or 'n' to return to array creation): \n")

    # call keepArray() to evaluate if array will be rerolled or not
    if keepArray(keep):
        opMenu(array)
    else:
        # unhappy with array --> restart array selection
        start()

    return


# method for user to build their own array
def byoArray():
    return


# initialize array with size of array as well as min and max values for the random generator range
def randArray():
    arr = []
    # gather array constraints from user input
    size = int(input("Enter array size: "))
    low = int(input("Enter lowest possible value for the array: "))
    high = int(input("Enter highest possible value for the array: "))

    # build array by appending n number of random elements
    for i in range(size):
        arr.append(random.randint(low, high+1))
    # print array
    print("Array size: " + str(size) + "   Minimum possible value: " + str(low) +
          "   Maximum possible value: " + str(high))
    print("\nRandom Array: " + str(arr))
    return arr


# option to reroll array
def keepArray(st):
    # true if user wants to keep array
    if st == 'y' or st == 'Y':
        return True
    # false if user wants new array
    elif st == 'n' or st == 'N':
        return False


# calculates sum of array
def sumArray(arr):
    total = 0
    # continuously add each element in array to total value
    for i in range(len(arr)):
        total += int(arr[i])
    return total


# calculates product of all array elements
def productArray(arr):
    # total starts at 1 (0 would always result in 0 for multiplication)
    total = 1
    # continuously multiply each elements in array with total value
    for i in range(len(arr)):
        total *= int(arr[i])
    return total


# returns new array with the square of each element
def squareArray(arr):
    sqrArr = []
    for i in range(len(arr)):
        sqrArr.append(pow(arr[i], 2))
    return sqrArr


# returns new array with the square root of each element
def sqrtArray(arr):
    sqrtArr = []
    for i in range(len(arr)):
        sqrtArr.append(math.sqrt(arr[i]))
    return sqrtArr


# adds up total number of even and odd numbers in original array
def evenOdd(arr):
    evenCount = 0
    oddCount = 0

    for i in range(len(arr)):
        # mod 2 == 0 means even
        if arr[i] % 2 == 0 or arr[i] == 0:
            evenCount += 1
        # else odd
        else:
            oddCount += 1
    # 2 outputs return as a list [evenCount, oddCount]
    return evenCount, oddCount


# determines if given number is prime or not
#   is a supporting function for primeCount
def isPrime(x):
    # start divisor at 2, since a prime is divisible by 1
    divisor = 2
    # loop until divisor would be == x, since a prime is divisible by itself
    while divisor < x:
        # test each int between 1 and x (exclusive) to see if any will evenly divide x
        if x % divisor != 0:
            divisor += 1
        # if for any divisor between 1 and x (exclusive), x mod divisor == 0, then x is not prime. return false
        else:
            return False
    # if all divisors fail to divide evenly, return true. x is prime
    return True


# build new array consisting of only the prime numbers from the original array
#   relies on isPrime()
def primeCount(arr):
    primes = []
    # test each array element to determine if its a prime
    for i in range(len(arr)):
        # append primes onto new prime array
        if isPrime(arr[i]):
            primes.append(arr[i])
    # return array of primes
    return primes


# converts an int x from base 10 to base b, where b can be any int between 2 and 32 (inclusive)
#   supporting function for baseConvertArray()
def baseConverter(x, b):
    # converted number in new base will be built as an array
    newNum = []
    # initialize quotient so it is not 0, thereby not interfering with while loop condition
    quo = 1

    # while quotient is not 0
    while quo != 0:
        # set quotient = number to be converted divided by the desired base conversion
        #   floor division so as to allow for remainder to be accurate
        quo = x // b
        # int remainder of above calculation
        rem = x % b

        # if remainder exceeds 9, thereby extending past decimal digits and requiring the english alphabet as symbols,
        # append onto array newNum the ascii character corresponding to the remainder value
        # ascii character 97 == 'a', so if remainder is 10, 10 + 87 = 97, 'a' is appended to newNum
        # ascii character 118 == 'v' (the highest possible digit in base 32)
        # remainders in between will correspond to a letter between a and v
        # in a more refined conversion calculator, 'i' and 'o' may need skipped over to avoid confusion with
        # numerals 0 and 1
        if rem > 9:
            newNum.append(chr(rem + 87))
        # is remainder is 9 or less, append remainder to newNum array
        else:
            newNum.append(rem)
        # set new x equal to quotient and repeat until quo == 0
        x = quo

    # array must be reversed to have accurate representation
    newNum.reverse()
    # return array of converted number in base b
    return newNum


# takes an input array of integers in base 10, along with a target base b, and outputs a new array with the
#   elements in the original array converted into base b
#       relies on baseConverter
def baseConvertArray(arr, b):
    # new array to store converted elements
    baseArr = []

    # loop through entire original array
    for i in range(len(arr)):
        # create an empty string at the start of each pass
        snip = ""
        # calls baseConverter with the current original array element and target base as parameters
        #   loops through returned array from baseConverter and builds a string from its elements
        #       this is to display the converted number as, for example, '1011' instead of ['1', '0', '1', '1']
        for s in baseConverter(int(arr[i]), int(b)):
            snip += str(s)
        # append newly built string onto new array
        baseArr.append(snip)
    # return new array of elements converted to target base
    return baseArr


start()
