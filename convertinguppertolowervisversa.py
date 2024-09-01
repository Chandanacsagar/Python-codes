str=input("enter a string: ")
newstr=" "
i=0
while(i<=len(str)-1):
    char1=str[i]
    ascii=ord(char1)
    if(ascii>=65 and ascii<=90): #upper 
        newascii=ascii+32
        convchar=chr(newascii)
        newstr=newstr+convchar
    elif(ascii>=97 and ascii<=122): #lower
        newascii=ascii-32 
        convchar=chr(newascii)
        newstr=newstr+convchar
    else:
        newstr=newstr+char1
    i=i+1
print(newstr)