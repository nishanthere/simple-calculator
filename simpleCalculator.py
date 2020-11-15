title = "This is a simple calculator developed by an IT-Major student"
print(title.upper())
print("It can do simple calculations like Addition,Substration,Multiplication,Division and Modulus")
print("------------------------------------")



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

def main():
    print("Select operation")
    print("1 for addition")
    print("2 for susbtraction")
    print("3 for multiplication")
    print("4 for division")
    print("5 for modulus")
    choice = int(input("Enter the operation: "))
    if choice == 1:
        add=addition()
    elif choice == 2:
        subs=substraction()
    elif choice == 3:
        mult=multiplication()
    elif choice == 4:
        div=division()
    elif choice == 5:
        modul=modulus()
    else:
        print("Error")

    
    

if __name__=="__main__":
        main()
