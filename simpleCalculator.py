import math

def addition():
    total=0
    times = int(input("How many numbers you want to calculate?: "))
    for i in range(1,times+1):
        No = int(input("Enter number: "))
        total = total + No
    print("On calculation gives:",total)

def substraction():
    Num1 = int(input("Enter 1st number: "))
    Num2 = int(input("Enter 2nd number: "))
    sub = Num1 - Num2
    print("On calculation gives: ",sub)

def multiplication():
    total=1
    times = int(input("How many numbers you want to calculate?: "))
    for i in range(1,times+1):
        No = int(input("Enter number: "))
        total = total * No
    print("On calculation gives:",total)


def division():
    Num1 = int(input("Enter 1st number: "))
    Num2 = int(input("Enter 2nd number: "))
    divi= Num1 / Num2
    print("On calculation gives: ",divi)
    

def modulus():
    Num1 = int(input("Enter 1st number: "))
    Num2 = int(input("Enter 2nd number: "))
    mod = Num1 % Num2
    print("On calculation gives: ",mod)
    
def percentage():
    total=0
    times= int(input("Enter the number of subjects: "))
    for i in range(1,times+1):
        No= int(input("Enter marks: "))
        total = total + No
    print("Your total marks are: ",total)
    per= float(total/500)*100
    print("Percentage is: ",per)

def exponentiation():
    base = int(input("Enter value of base: "))
    exponent = int(input("Enter value of exponent: "))
    print("Exponential value is: ",pow(base,exponent))

def main():
    print("Select operation")
    print("1 for addition")
    print("2 for susbtraction")
    print("3 for multiplication")
    print("4 for division")
    print("5 for modulus")
    print("6 for percentage")
    print("7 for exponentiation")
    choice = int(input("Enter the operation: "))
    if choice == 1:
        addition()
    elif choice == 2:
        substraction()
    elif choice == 3:
        multiplication()
    elif choice == 4:
        division()
    elif choice == 5:
        modulus()
    elif choice == 6:
        percentage()
    elif choice == 7:
        exponentiation()
    else:
        print("Error")
    choice1 = str(input("If you want to re-use, press 'a':"))
    if choice1 == str("a"):
        main()
    else:
        print("Thankyou and Goodbye :)")


if __name__=="__main__":
        main()
