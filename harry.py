"""class person :
    name="harry"
    occupation="software development"
    networth=10
    def info(self):
     print(f"{self.name}is a {self.occupation}")
 

a = person()
#a.name="sanket"
#.occupation="accountance"
#print(a.name, a.occupation)
a.info()
class person():
   cc = "fff"
   def info(self):
    print(f"{self.cc}is in")
a=person()
a.info()
#tutorial no 58
class person:
    name="harry"
    occ="developer"
    def info(self):
        print(f"{self.name}is {self.occ}")
a=person()
a.name="sanket"
a.occ="farm"
a.info()

#matrics multiflication
A =[[1,5,7],
   [4,7,7],
   [4,2,7]]
B= [[3,5,3],
    [4,6,3],
    [9,6,7]]    
 
C= [[0,0],
    [0,0],
    [0,0]]


for i in range(0,len(C)):
    for j in range(0,len(C[0])):
        for k in range(0,len(B)):
            C[i][j] += A[i][k] * B[k][j]

for row in C:
    print(row)
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


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


\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
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
