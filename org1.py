import re
import datetime
f=open("things.txt","r")
t=datetime.datetime.now()
f.write("your total 200\n{t}")

f=open("things.txt","r")
x=f.read()
your_word=input("enter your word : ")
y=re.search(your_word,x)
print(y)

print("your word is their" if y else "not their")













#print("***seven* supermarket order***")
#print("\nROW 1 : drink \nROW 2 : cookies \nROW 3 : snacks \nROW 4 : cereal  \nROW 5 : forzen food")




