import math

n = int(input("n?: "))

def getSum(n):

    sum = 0
    for digit in str(n):
      sum += int(digit)
    return sum

dsum = (getSum(n))

if n != [2,5]:
    # if n % 2 != 0:
    #     if dsum % 3 != 0:
    #         # if n != 5:
    #         #     if int(repr(n) [-1]) !=5:
    #         #         # if n > 100
    #         #         #     n = (math.sqrt(n))
    #         #
    #         #         # else (add n to list)
    #         #
    #         #
    #         #         print ("Prime?")
    #         #
    #         #     else:
    #         #
    #         #         print ("Definitely not prime")
    #         #
    #         # else:
    #         #
    #         #     print ("Prime")
    #
    #     else:
    #
    #         print ("Definitely not prime")
    #
    # else:
    #
    #     print ("Definitely not prime")

else:

    print ("2 or 5")
