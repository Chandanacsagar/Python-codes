# Duck Number--> is a positive number should contain atleast on zero in it but that number should not start with zero

# Using Bult-in:

def duck(n):
    num=str(n)
    num=num.lstrip('0')
    if '0' in num:
        return True
    else:
        return False
n=int(input())
if duck(n):
    print("Duck number")
else:
    print("Not a duck number")
 
#-------------------------------------------------------------------------------
   
# Without using Bult-in:

def duck(n):
    num=str(n)
    if num[0]=='0':
        return False
    for digit in num:
        if digit=='0':
            return True
    return False
n=int(input())
if duck(n):
    print("Duck number")
else:
    print("Not a Duck Number")