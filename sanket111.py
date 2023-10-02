

"""def square(n):
    print(n**2)
square(5)

def square(n):
    print(n*7)
square(5)

'''takema number'''
print(square.__doc__)"""
#factorial=7*6*5*4*3*2*1def square(n):

  #factorial program
"""def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
     return n * factorial(n-1)
print(factorial(4))
"""
"""#set is collectionn of well defind object
s={2,4,3,52,2}
print(s)
#it is unorderd data collection. set is unchangeble 
info={"harry",12,3}
print(info)
harry=set()
print(type(harry))
for value in info:
    print(value)
s1={1,2,4,6}
s2={3,5,3,2}
print(s1.union(s2))
s1.update(s2)
print(s1,s2)
"""
#cities={"satara","kolahapu","patan"}
#cities2={"satar","karad","pune"}
#cities3=cities.difference(cities2)
#print(cities3)

# n* facdtorial (n-1)
"""def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
print(factorial(10))"""
# 5*factorial(4)
# 5*4*factorial(3)
#5*4*3*factorial(2)
#5*4*3*2(1)

"""fibonicees series
f0=0
f1=1
f2=f1+f0
f(n)=f(n-1)+f(n-2)

def f(n)
    if(n<1):
    return 1
    else:
       return n* f(n-1)
print(f(3))
"""
"""""
s1={1,2,3,}
print(s1)
s2={3,4,5,}
#print(s1.union(s2))
s1.update(s2)
print(s1)
print(s1.issuperset(s2))
print(s1.issubset(s2))
"""


"""dic={
    "name":"harry",
    22:"sanket",
    56:"raj"
}
#print(dic)
#print(dic[333])
print(dic.get('name'))
for key in dic.keys():
    print(dic[key])
"""
# 34 tutorial
#ep={122:45,123:89,68:33}
#ep2={222:32,34:44}
#ep.update(ep2)#
# ep.clear()
#ep.pop(122) value kadhane
# ep.popitem() remove last item
#del ep[122]  paython dictonary documentation  search 
#print(ep)


# 35 tutorial : 0 to n-1 range
"""for i in range(6):
    print(i)
    if i == 4:
        break
else:
    print("i am sorry")
"""
"""i=0
while i<710:
    print(i)
    i=i+1
    """


"""
#tutorial no :36
a= input("enter a number ")
print(f"multiflication tabl{a}")
try:
   for i in range(1,11):
    print(f"{int(a)}x{i}={int(a*i)}")
except Exception as e:
 print("sorry some erroris occurs")
    
"""
 
"""
 #tutourial no 37

#func1():
try:
    l=[1,2,3]
    i=int(input("enter the index "))
    print(l[i])
except:
    print("so,e error is occurs")

finally:
  print("i am alwas is executed")
"""
"""
#tutorial no :38
a=int(input("enter value betweeen 5 and 9"))
if(a<5 or a>9):
  raise ValueError("valu should be between 5 and 9")
# paython error calsses serch on the google 
++
"""

# tutorial no 39
# kon banega karodapati 
"""
questions=[
              ["which language was use to create facebook?","paython",
          "french","javascript","php","none",4],
              ["2)indias national bird?","peecock",
               " cock","cat","dog","man",1],
              ["national animal of india ?","lion ",
                   "tiger","elephant","dog","none",2],
                 ["national flower of indai?","rose",
                   "white flower","lotus","no of the","none",3],
                   [ "india capital name is","dheli","mumbai","panjab","satara","thane",1]


]         
levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000]

money=0
   # def ask_questions(questions):
    #print(questions)
 
for i in range(0,len(questions)):
    question= questions[i]
   
   # Print the first question



    print(f"\n\nouestion for rs {levels[i]}")

      print(f"")
    reply= int(input("enter your answer (1-4)"))
    if(reply==question[-1]):
        print(f"correct answer ,you have won rs {levels[i]}")
        if(i== 4):
            money = 10000
        elif(i==9):
         money=320000
    else:
        print("wrong answer")
        break
print(f"your take home money is {money}")


"""
"""
questions = [
    ["Which language was used to create Facebook?", "Python", "French", "JavaScript", "PHP", "None", 4],
    ["India's national bird?", "Peacock", "Cock", "Cat", "Dog", "Man", 1],
    ["National animal of India?", "Lion", "Tiger", "Elephant", "Dog", "None", 2],
    ["National flower of India?", "Rose", "White flower", "Lotus", "No of these", "None", 3],
    ["India's capital name is?", "Delhi", "Mumbai", "Punjab", "Satara", "Thane", 1]
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]

money = 0

for i in range(len(questions)):
    question = questions[i]
    print(f"\nQuestion for Rs {levels[i]}:")
    print(question[0])
    for j in range(1, 5):
        print(f"{j}. {question[j]}")
    
    reply = int(input("Enter your answer (1-4): "))
    
    if reply == question[-1]:
        print(f"Correct answer! You have won Rs {levels[i]}")
        if i == 4:
            money = 10000
        elif i == 9:
            money = 320000
    else:
        print("Wrong answer")
        break

print(f"Your take-home money is Rs {money}")
"""

"""
#tutorial no 40  for coding the messege

choice = input("To Code Message Press 1 To Decode Message Press 2: ")
if(choice == "1"):
  msg = input("Enter The Message To Be Coded: ")
  if(len(msg) > 3):
    encode1 = msg[1:] + msg[0]
    encode2 = msg[2:5] + encode1 + msg[0:3]
    print(encode2)
  
  else:
   print(msg[::-1])
  

elif(choice == "2"):
   msg =  input("Enter The Code: ")
   if(len(msg) >3):
    step1 = msg[:-3]
    step2 = step1[3:]
    step3 =step2[-1] + step2[:-1]
    print(step3)

   else:
    print(msg[::-1])
    
else:
    print("Invalid Operation")
    """

#  tutorial no 41
"""
a=330000
b=3300
print("A") if a>b else print("=") if a==b else print("B")
c=9 if a>b else 0
print(c)
"""
"""
#tutorial no 42
marks = [10,33,57,57,43,88,33,98,65]
index=0
for mark in marks:
    print(mark)
    if(index == 3):
        print("harry,awsome")
    index +=1
    """
"""
marks = [10,33,57,57,43,88,33,98,65]

for index, mark in enumerate(marks):
    print(mark)
    if(index == 0):
        print("harry,awsome")
    index +=1
    """

#tutorial no 44
"""import math
#math.floor(4.2343)
from math import pi,sqrt as s
result=s(9)*pi
print(result)

import math
print(dir(math))
print(type(math.cos))

"""
#tutorial no 45

#tutorail no 46
#tutorial 47
"""
st=input("enter messege\t")
words=st.split(" ")
coding= input(" 1 for coding and 0 for decoding")
coding= True if (coding=="1") else False
print(coding)
if(coding):
    nwords = []
    for word in words:
        if(len(word)>=3):
            r1="dsg"
            r2="por"
            stnew=r1+word[1:] + word[0]+r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
        print(" ".join(nwords))

else:
    nwords=[]
  """
"""

#tutorial no :48
x=10#golbal variable

def my_function():
    global x # for changing variable
    x=1
    y=5
    print(y)#locakl variable
    print(x)

my_function()
"""
"""
#tutorial n0 49:
print(8)
f = open('sanket.py','r')
print(f)
text = f.read()
print(text)
f.close()

#tutorial no 50
f=open('harry.py','r')
while True:
    line = f.readline()
    print(line)
    if not line:
        print(line,type(line))
        break

f=open('san.py','w')
lines=['line 1\n','line 2']
f.writelines(lines)
f.close()

#tutorial no 51
f=open('harry.py','r')
f.seek(15)#moves currnt position to onwords read drop 1st charecter 
text=f.read()
#print(f.tell())

print(text)
print(type(text))

double= lambda x:x*2
print(double(4))

# tutorial 53 reamening
def cube(x):
   return x *x * x
print(cube(2))
l = [3,5,6,7]
#newl=[]
#for item in l:
 #   newl.append(cube(item))
 newl = list(map(cube, l))
 print(newl)
 
#tutorial no 54
a= (1,2)
b= (1,2)
print(a is b) #Exact location of object memory
print(a==b)#value
 
 # tutorial no 55

print("choose one of the option\n1.snake \n2.water \n3.gun")
int(input("enter your choice "))
 
class person :
    name="harry"
    occupation="software development"
    networth=10
a=person()
a.name="sanket"
a.occupation="accountance"
print(a.name,a.occuppation)


import random
def check(comp,user):
    if comp==user :
        return 0
    if(comp==0 and user==2):
        return -1
    if(comp==1 and user==0):
        return -1
    if(comp==2 and user==1):
        return -1
    return 1
    
comp=random.randint(0,2)
user=int(input(" 0]STONE\n 1] PAPER\n 2] SCISSORS\nchoose on of them "))
score=check(comp,user)

print("you: ",user)

print("computer: ",comp)
if(score ==0):
 print("IT IS A DRAWP 🙌")
elif(score== -1):
    print("YOu LOSS GAME 😭")
else:
    print("...........congractulation...........")
    print("YOU WON GAME 👍")

print(".....................GAME IS OVER......................")

class Library:
    def __init__(self):
        self.noBooks =0
        self.books=[]
    def addBook(self,book):
        self.books.append(book)
        self.noBooks = len(self.books)
    def showInfo(self):
        print(f"the library has {self.noBooks}")

li=Library()
li=addBook(" harry potter")
li.showInfo() 
       
#x=(1,3,5)
#print(dir(x))
#print(x.__add__)
class person:
    def __init__(self,name,age) -> None:
        self.name=name
        self.age =age
p= person("san",30)
print(p.__dict__)
print(help(person))
  #billing of the prices code     
sum=0
while(True):
    userInput= input("Enter the price and press q for quite:\n")
    if (userInput !='q'):
     sum = sum+ float(userInput)
     print(f"order total so far : {sum}$\n")
    else:
     print(f"your bill is {sum}$ ")
     print("thanks for coming our shop")
     break
     
      

def factorial(num):
    if num==0 or num==1:
        return 1
    else:
        return num* factorial(num-1)
num=int(input("enter a number "))
fac=factorial(num)
print(f"factorial is  {fac}")

""" 

