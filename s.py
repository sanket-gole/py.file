"""print("harry is good","sanket is good")
var="hell"
var2=4.4
print(var)
print(type(var2))
var3="22"
var4="33"
#print(100*str(int(var3)+int(var4)))
#print(10*"hello world\n")

print("enter a number ")
innum=input()
print("you enterd",int(innum)+5)
print("enter first number ")
n1=int(input())
print("enter second num")
n2=int(input())
print("addition is",n1+n2)


my="harry is agood boy"
print(len(my))
print(my[-4:-2])
print(my.count("b"))
print(my.capitalize())
print(my.upper())
print(my.replace("is","by"))
"""

#grocery= ["harpic","vim bar ","bhindi","lolypop",66]
#print(grocery[4])
#numbers=[2,4,66,56,7,4]
#numbers.sort()
#numbers.reverse()
#numbers.append(5)
#
#numbers.insert(2,36)
#numbers.remove(2)
#numbers.pop() last element delete
#numbers[1]=98
#print(numbers)
# list is :mutable  tuple is inmutable
#tp=(1,3,4) # paranthisis
#tp[1]=2
#tp(1,)#for tupple one element
#a=1
#b=8
#a,b=b,a
#print(a,b)
#temp=a
#a=b
#b= temp
#print(tp)


# dictiomnary is nothing but key valu pair
#d={ "harry":"burger","rohan":"fish","sanket":{"b":"maggi","l":"pohe","d":"chaha"}}
#print(d["sanket"])


# write program to make dictionary and take input from user and w
3#write meaning
"""
dict={"sanket":"gole","pg":"patil","rk":"naik"}
use=input()

print(dict[use])
"""
s=set()
#print(type(s))
#s_from_list = set([1,3,4,5])
#print(s_from_list)
#s.add(1)
#s.add(2)
#s1=s.union({5,5,6,7})
#print(s,s1)
"""
var1=44
var=33
var3=int(input())
if var3>var1 :
    print("greter")
elif var==var3:
    print("equal")
else:
    print("less")
 
print("enter your age ")
age=int(input())
if age>18:
    print("you can drive")
elif age==18:
    print("we cant decide")
else:
    print("you cant drive")
    
    
   
i =0
while(True):
    if i+1<5:
        i=i+1
        continue
    print(i+1,end="  ")
    if(i==44):
        break
    i=i+1

while(True):
  inp=int(input())
  if inp>100:
    print("you enterd num isgreter then 1oo")
    break
  else:
    print("try again")
    continue
   
list=[["harry",1],["larry",44],["marry",56],["carry",67]]
#print(list)
for item, lollypop in list:
    print(item,"lolly is",lollypop)
"""