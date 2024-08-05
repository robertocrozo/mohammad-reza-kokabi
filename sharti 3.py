num1 = int(input("give number 1  :"))
num2 = int(input("give number 2  :"))
num3 = int(input("give number 3 :"))
num4 = int(input("give number 4 :"))
all = (num1 + num2 +num3 +num4)
avg = (all/4)

print(f"avrege of your 4 number if : {avg}")
if (avg>=18):
    print("you are A")
elif (avg>=16):
    print("you are B")
elif (avg>=14):
    print("you are C")
elif (avg>=10):
    print("you are D")
else:
    print("faild")
