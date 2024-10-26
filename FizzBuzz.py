def fizzbuzz(n):
    if n%3==0 and n%5==0:
        return  "FizzBuzz"
    elif n%3==0:
        return "Fizz"
    else:
        return "Buzz"
n=int(input())
res=fizzbuzz(n)
print(res)

#------------------------------------------------------------------------------------------

def fizzbuzz(n):
    return n
sr=int(input("enter 1st number: "))
er=int(input("enter 2nd number: "))
if sr>er:
    print("invalid")
else:
    print("FizzBuzz")
    for i in range(sr,er+1):
        if i%3==0 and i%5==0:
            print(i)
    print("Fizz")
    for i in range(sr,er+1):
        if i%3==0:
            print(i)
    print("Buzz")
    for i in range(sr,er+1):
        if i%5==0:
            print(i)
    print("not FizzBuzz")
    for i in range(sr,er+1):
        if i%3!=0 and i%5!=0:
            print(i)