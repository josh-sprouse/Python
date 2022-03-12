# 6.Write a program that asks the user for a number n and gives them the possibility to choose between computing the ans and computing the product of 1,…,n.

num = int(input("Input a number: "))
choice = input("(S)um or (P)roduct to 1? ")


if str.lower(choice) != ("s"):
    if str.lower(choice) != ("p"):
        choice = input ("Please enter (S) for sum or (P) for product ")

if str.lower(choice) == ("s"):

    ans = 0

    while num > 0:

        ans += num
        num -= 1

    else:
        print (ans)

elif str.lower(choice) == ("p"):

    ans = 1

    while num > 0:

        ans *= num
        num -= 1

    else:
        print (ans)
