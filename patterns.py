## BAISC PATTERNS:

# print('*')

# for j in range(1,4+1):
#     print('*')

# for j in range (1,4+1):
#     print("*",end="")   
    
# n=int(input())
# for i in range(1,n+1):
#     for j in range (1,i+1):
#         print((j+i+1)%2,end=" ")
#     print()


#-------------------------------------------------------------------------------------------------------------

## LEFT PATTERN:

# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

## INVERTED LEFT PATTERN:

# n=int(input())
# for i in range(1,n+1):
#     for j in range(n,i-1,-1):
#         print("*",end="")
#     print()

#---------------------------------------------------------------------------------------------------------------

## LEFT MIRROR PATTERN:

# n=int(input())
# for i in range(1,n+1):
    # for j in range(n,i,-1):
    #     print(" ",end="")
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()


## INVERTED LEFT MIRROR PATTERN:

# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,i):
#         print(" ",end=" ")
#     for j in range(n,i-1,-1):
#         print("*",end=" ")
#     print()
 
#---------------------------------------------------------------------------------------------------------------

## PYRAMID PATTERN:
    
# n=int(input())
# for i in range(1,n+1):
#     for j in range(n,i,-1):
#         print(" ",end="")
#     for j in range(1,i+1):
#         print((j-1),end=" ")
#     print()

## INVERTED PYRAMID PATTERN:
    
# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,i):
#         print(" ",end="")
#     for j in range(n,i-1,-1):
#         print("*",end=" ")
#     print()
#---------------------------------------------------------------------------------------------------------------------

## COMBINATIONAL PATTERNS:

# n=int(input())
# noc=0
# for i in range (1,(n*2)):
#     if i<=n:
#         noc=noc+1
#     else:
#         noc=noc-1
#     for j in range(1,noc+1):
#         print(i,end=" ")
#     print()
    
# n=int(input())
# noc=1
# for i in range(1,(n*2)):
#     for j in range(n,noc,-1):
#         print(" ",end=" ")
#     for j in range(1,noc+1):
#         print("*",end=" ")
#     print()
#     if i<n:
#         noc +=1
#     else:
#         noc -=1


#----------------------------------------------------------------------------------------------------------------

# n=int(input())
# for i in range(1,n+1):
#     for j in range (1,i+1):
#         print((j+i+1)%2,end=" ")
#     print()
    
# n=int(input())
# for i in range(1,n+1):
#     for j in range(n,i-1,-1):
#         print(" ",end="")
#     for j in range(n,n-i,-1):
#         print(j,end=" ")
#     print()
   
# n=int(input())
# noc=n
# for i in range(1,(n*2)):
#     for j in range(1,noc+1):
#         print("*",end=" ")
#     print()
#     if i<n:
#         noc -=1
#     else:
#         noc +=1

# n=int(input())
# noc=n
# for i in range(1,(n*2)):
#     for j in range(n,noc,-1):
#         print(" ",end=" ")
#     for j in range(1,noc+1):
#         print("*",end=" ")
#     print()
#     if i<n:
#         noc -=1
#     else:
#         noc +=1
    