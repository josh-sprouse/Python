# 4. Write a program that asks the user for a number n and prints the sum of the numbers 1 to n

num = int(input("Input a number: "))
sum = 0


while num > 0:

    sum += num
    num -= 1

else:
    print (sum)
