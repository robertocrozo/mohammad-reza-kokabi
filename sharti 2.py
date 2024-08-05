num1 = int(input("give number 1  :"))
num2 = int(input("give number 2  :"))
num3 = int(input("give number 3 :"))
if (num1 >= num2):
    if (num1 >= num3):
        print(f"{num1}is the biggest")
elif (num2 >= num1):
    if (num2 >= num3):
        print(f"{num2}is the biggest")
elif (num3 >= num1):
    if (num3 >= num2):
        print(f"{num3}is the biggest")