num = int(input("give number :"))
if num % 15 == 0:
    print ("fizz buzz!")
elif num % 3 == 0:
    print ("fizz!")
elif num % 15 == 0:
    print ("buzz!")
else : print("invalid number")