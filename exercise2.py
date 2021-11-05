mail = str(input("Please enter your e-mail adress: "))
a = mail.count("@")
b = mail.count(".")

if a == 1 and b >= 1 :
    print("This is a valid e-mail adress.")
else:
    print("Sorry, this is not a valid e-mail adress.")