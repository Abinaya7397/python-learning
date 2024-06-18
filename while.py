'''
#write a progra to the reverse number
num1=int(input("enter the number"))
r=0
rnum=0
while(num1!=0):
    r=num1 % 10
    rnum=rnum*10+r
    num1=num1//10
    print("reverse number is :",rnum)
   ''' 
'''
#write a program to print first 10 integer and their squares
num=1
print("numbers\t\tsquares")
while(num<=20):
    print(num,"\t\t",num**2)
    num=num+1
'''
'''
#to print tabe of contert entered from the user
i=1
num=int(input("enter the number : "))
while  i<=10:
    print(i,"*",num,"=",i*num)
    i=i+1
'''
'''
#to print all te characters in the string "Abinya"
str="abinaya"
i=0
while(i<len(str)):
    print(str[i])
    i=i+1
'''
#factorial number accepter from the user
num=int(input("enter the number : "))
f=1
i=1
while(i<=num):
    f=f*i
    i=i+1
    print("factorial number is :", f)