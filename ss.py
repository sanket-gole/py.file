"""a = int(input("enter a"))
b=int(input("b"))
if a>b: print("a is big")
else: print("b is big")

a=9
b=8
c=sum((a,b))# built in function
print(c)

def func1(a,b):
  
print(func1.__doc__)



print("enter num1")
num1=input()
print("enter num 2")
num2=input()
try:
    print("the sum is",
          int(num1)+int(num2))
except Exception as e:
    print(e)
print("this line is imp")
"
f=open("main.py","rt")
#r=f.read()
#for line in r:
print(f.readlines())









f.close()

f=open("main.txt","w")
a=f.write("harry is good\n")
print(a)
f.close()
f = open("main.txt","r+")
print(f.read())
f.write("thank you")



one=int(input())
print("type 1 or 0")
two=int(input())
new=bool(two)
if new == True:
    for i in range(1,one+1):
        for j in range(1,i+1):
            print("*",end="")
        print("")
elif new==False:
    for i in range(one,0,-1):
        for j in range(1,i+1):
            print("*",end="")
        print()

      


a=input()
if a==1:
   f=open("main.txt")
   s=f.readlines()
   print(s)"""