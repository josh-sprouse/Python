#5. Modify the previous program such that only multiples of three or five are considered in the sum, e.g. 3, 5, 6, 9, 10, 12, 15 for n=17

num = int(input("Input a number: "))
sum = 0


while num > 0:

    if num % 3 == 0:
        sum += num
        num -= 1

    elif num % 5 == 0:
        sum += num
        num -= 1

    else:
        num -= 1

else:
    print (sum)
