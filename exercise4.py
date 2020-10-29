print('HALLO\nCongatulations, in our calculator')

print("If you want finish write 'STOP'")
Dia = input("Enter operation: ")




import sys

def sum(a,b):

    print("{}+{}={:.1f}".format(a,b,float(a)+float(b)))

def riz(a,b):
    print("{}-{}={:.1f}".format(a,b,float(a)-float(b)))

def dob(a,b):
    print("{}*{}={:.1f}".format(a,b,float(a)*float(b)))

def chas(a,b):
    print("{}/{}={:.1f}".format(a,b,float(a)/float(b)))

while True:

    if Dia == '+':
        a = input("Enter First Number: ")
        b = input('Enter Second Number: ')
        if a== "STOP" or b== "STOP":
            print("Program finished!")
            sys.exit()
        else:
            sum(a, b)
    elif Dia == "STOP":
        sys.exit()
    elif Dia == '-':
        a = input("Enter First Number: ")
        b = input('Enter Second Number: ')
        if a== "STOP" or b== "STOP":
            print("Program finished!")
            sys.exit()
        else:
            riz(a,b)
    elif Dia == '*':
        a = input("Enter First Number: ")
        b = input('Enter Second Number: ')
        if a== "STOP" or b== "STOP":
            print("Program finished!")
            sys.exit()
        if a== "STOP" or b== "STOP":
            print("Program finished!")
            sys.exit()
        else:
            dob(a,b)
    elif Dia == '/':
        a = input("Enter First Number: ")
        b = input('Enter Second Number: ')
        if a== "STOP" or b== "STOP":
            print("Program finished!")
            sys.exit()
        else:
            try:
                chas(a,b)
            except:
                print("На "+ str(b) + " ділити не можна!")

    else:
        print('Operation did not found!')
        sys.exit()


