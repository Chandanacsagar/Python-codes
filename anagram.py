def anagram(str,str1):
    str=str.lower()
    str1=str.lower()
    a=sorted(str)
    b=sorted(str1)
    if a==b:
        return True
    else:              
        return False
str=input()
str1=input()
res=anagram(str,str1)
if res:
    print("anagram")
else:
    print("not a anagram")