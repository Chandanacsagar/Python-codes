num=int(input("Enter a number: "))
isdivisible=False
i=2
while i<num:
    if num % i==0:
        isdivisible=True
        print("{} is divisible by {}".format(num,i))
    i +=1
if isdivisible==True:
    print("the number is not prime",num)
else:
    print("the number is prime",num)