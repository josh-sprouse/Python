# 3. Modify the previous program such that only the users Alice and Bob are greeted with their names.

name = input("What's your name? ")

if str.lower(name) == ("alice"):
    print ("Greetings," , str.title(name))

elif str.lower(name) == ("bob"):
    print ("Greetings," , str.title(name))

else:
    print ("Heck you")
