# 7. Write a program that prints a multiplication table for numbers up to 12.

x = 1
y = 1
tab = None

while x < 13:
    while y < 13:

        tab = str(x) + "x" + str(y) + "=" + str(x*y) + "  "
        y += 1
        print (tab, end = "")

    else:
        x += 1
        y = 1
        print (end = "\n")
       
