try: 
    for i in ['a','b','c']:
        print(i**2)
except TypeError:
    print("Ahh, it'a  Type Error :(")


x = 5
y= 0
try: x/y
except ZeroDivisionError:
    print("Oops")


def ask():
    loop = True
    while loop:
        num = input("Input an integer:  ")
        try: int(num)
        except: print("Oops, it's not an integer")
        else:
            num = int(num)
            print(num**2) 
            loop = False

ask()