# AUTOMORPHIC NUMBERS--> if and only if its square ends in same digit as the number itself.

# Using BUILT-IN:
def automorphic(number):
    square=number**2
    str_num=str(number)
    str_squ=str(square)
    if str_squ.endswith(str_num):
        return True
    else: 
        return False
number=int(input())
if automorphic(number):
    print("automorphic")
else:
    print("not automorphic")
#-----------------------------------------------------------------------------------------

# without using BUILT-IN:
def automorphic(number):
    square=number**2
    n=len(str(number))
    last=square%pow(10,n)
    if last==number:
        return True
    else:
        return False
number=int(input())
if automorphic(number):
    print("automorphic")
else:
    print("not automorphic")
#----------------------------------------------------------------------------------------   
def automorphic(number):
    square=number**2
    n=len(str(number))
    last=square%pow(10,n)
    if last==number:
        return True
    else:
        return False
sr=int(input("enter a 1st number: "))
er=int(input("enter a 2nd number: "))
if sr>er:
    print("invalid input")
else:
    print("Automorphic numbers: ")
    for i in range(sr,er+1):
        if automorphic(i):
            print(i)