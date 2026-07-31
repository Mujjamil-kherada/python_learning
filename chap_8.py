# def percentage(marks):
#     return ( sum(marks)/400)*100

# mohib_per=percentage([40,40,50,60])
# print(mohib_per)

# def pattern_asc(n):
#     for i in range(1,n+1):
#         print("*",i)
# pattern_asc(4)

# def f(x):
#     x=x + 4# no return!
#     if x == 0:
#         return
# print(f(5))

# def car(name):
#     print("which car do you want",name)
# car(",BMW")

# def phone(name):
#     print("your phone is",name)
# phone("iphone 13")


# def numbers():
#     for num in range(1,21):
#         print(num)
# numbers()

# def fac_nb():
#     num=int(input("enter the num :"))
#     result=1
#     for i in range(1,num+1):
#         result*=i
#         print(f"Ans is {result}")
# fac_nb()

# def print_squre()
#     n=3 
#     for i in range(n):
#         if i==0 or i==n-1:
#             print("*"*n)
#         else:
#             print("*",end="")
#             print(" "* (n-2)+"*")
# print_squre()            

# def table():
#     number = 3
     
#         print(f"Table of {number}")
#         for num in range(1, 11):
#                 ans = number * num
#                 print (f"{number} X {num} = {ans}")
# table()


# def multiplication():
#     number = 3
#     for num in range(10,0,-1):  
#         ans = number * num
#         print (f"{number} X {num} = {ans}")
# multiplication()


# def print_X():
#     n=10
#     for i in range(n):
#         for j in range(n):
#             if i==j or i+j==n-1 :
#              print("*",end="")
#             else:
#                 print(" ",end="")
#         print()
# print_X()

# def infinite():
#     number=[7]
#     unlimited=len(number)
#     start=0
#     while unlimited>start:
#         print(number[start])
# infinite()      
# 

# def num_():
#     number=int(input("Enter your number :"))
#     while number<=10:
#         print("NUmber printed by program : ",number)
#         number=1
#     names=[10,20,30,40,50]
#     _len=len(names)
#     start=0
#     while _len>start:
#         pass
# num_()  

# {recursion}------------------->

# def rec_fn(number):
#     if number==1 or number==0 :
#         return 1
#     return number * rec_fn(number-1)
# print(rec_fn(5))
    
# sum=0
# for num in range(1,101):
# sum=+

# def sum(num):
#     if num==1:
#         return 1
#     return num+sum(num-1)
# number=int(input("Enter the number for plus :"))
# print(sum(100))

# ans 1----------->

# def greatest(a,b,c):
#     if a>=b or a>=c:
#         return a
#     if b>=a or b>=c:
#         return b
#     else:
#         return c

# number1=int(input("Enter the number 1 for plus :"))
# number2=int(input("Enter the number 2 for plus :"))
# number3=int(input("Enter the number 3 for plus :"))
# print("Max num is: :",greatest(number1,number2,number3))

# ans 3----->

# print("1st line :", end="@@@@@@@")
# print("2nd line")

# ans 6------>

# def cm(n):
#     return n*2.5
# num=float(input("enter the num for convert"))
# print(cm(num))

# ans 7-------->

# list_1=["mujju","mohib"," sami","ayan","sami "]

# def remove_list(l,name):
#     new_l=[]
#     for item in l:
#         if item != name.strip():
#             print(item)
#             new_l.append(item.strip())
#     return new_l
# print(remove_list(list_1,"sami"))

# ans 2------------->

# def celsius_to_fahrenheit(celsius):
#     return (celsius * 9/5) + 32

# print(celsius_to_fahrenheit(10))\

# ans 5---------->

# def pattern_desc(n):
#     print(f"\nPattern: Decreasing Triangle (n={n})")
#     for i in range(n, 0, -1):
#         print("* " * i)

# pattern_desc(3)

# 8----?

