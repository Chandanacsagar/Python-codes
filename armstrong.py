# ITERATIVE:

# def countDigit(n):
#     count=0
#     while n!=0:
#         n//=10
#         count+=1
#     return count
    
# n=int(input())
# temp=n
# sum=0
# pow=countDigit(n)
# while n!=0:
#     base=n%10
#     sum=sum+(base**pow)
#     n//=10
# if temp==sum:
#     print("armstrong")
# else:
#     print("not armstrong")

# FUNCTION:

# def countDigit(n):
#     count=0
#     while n!=0:
#         n//=10
#         count+=1
#     return count
# def check(n):    
#     temp=n
#     sum=0
#     pow=countDigit(n)
#     while n!=0:
#         base=n%10
#         sum=sum+(base**pow)
#         n//=10
#         if temp==sum:
#             return True
#         else:
#             return False
# n=int(input())
# if check(n):
#     print("armstrong")
# else:
#      print("not armstrong")

# RECURSION:

# def countDigit(n):
#     count=0
#     while n!=0:
#         n//=10
#         count+=1
#     return count
# def check(n,sum,temp,pow):
#     if n==0:
#         return temp==sum
#     base=n%10
#     sum=sum+(base**pow)
#     return check(n//10,sum,temp,pow)
# n=int(input())
# pow=countDigit(n)
# flag=check(n,0,n,pow)
# if flag==True:
#     print("armstrong")
# else:
#     print("not armstrong")


def countDig(n,count):
    if n==0:
        return count
    return countDig(n//10,count+1)
n=int(input())
res=countDig(n,0)
print(res)
    
    

