# def add(a,b):
#     return a+b
# def subtract(a,b):
#     return a-b
# def multiply(a,b):
#     return a*b
# def division(a,b):
#     if b!=0:
#         return a/b
#     else:
#         return "Cannot divide by zero"
# num1=float(input("Enter the First Number"))
# num2=float(input("Enter the Second Number"))

# print("Select the available options")
# print("1. Addition")
# print("2. Subtraction")
# print("3. Multiplication")
# print("4. Division") 

# choice=input("enter your choice(1/2/3/4): ")
# if choice in ('1','2','3','4'): 
#      if choice=='1':
#            result=add(num1,num2)
#      elif choice=='2':
#             result=subtract(num1,num2)
#      elif choice=='3':
#             result=multiply(num1,num2)
#      elif choice=='4':
#             result=division(num1,num2)
#      print(f"Result:{result}")
# else:
#      print("Invalid Choice")
            
#---------------------------------------------------------------------------------------------------------

class calci:
    def operation(self,a,b):
        c=a+b
        c1=a-b
        c2=a*b
        c3=a/b
        return c,c1,c2,c3
c1=calci()
x=5
y=2
r1,r2,r3,r4=c1.operation(x,y)
print(r1)
print(r2)
print(r3)
print(r4)