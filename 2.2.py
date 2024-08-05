fname = (input("give us your first name   :"))
lname = (input("give us your last name   :"))
age = int(input("give us your age   :"))
if age > 0 and age <100:
    print (fname + " "+ lname,age)
    print (f"your first name if {fname} and your last name is {lname} . so your full name is {fname+lname} . your age is {age}")
    print ("your first name if {} and your last name is {} . so your full name is {} . your age is {}" format (fname, lname, fname+lnmae, age))