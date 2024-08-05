num1 = int(input("give me your first number : "))
num2 = int(input("give me your seocound number : "))
op = input("give me betwen (+, -, *, /, ) :")
if op == "+":
    print (num1, "+", num2, num1+num2)
elif op == "-":
    print (num1, "-", num2,"=",  num1-num2)
elif op == "*":
    print (num1, "*", num2,"=",  num1*num2)
elif op == "/":
    print (num1, "/", num2,"=", num1/num2)
else :
    print ("Invalid op")



