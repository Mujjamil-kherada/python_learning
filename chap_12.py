# a=input("Input karo")
# try:
#     print
# while True:
#     print("Bank chalu che")
#     case_depo=int(input("Enter the value"))
#     balance=100
#     output=0
#     try:
#         output=balance/case_depo
#     except Exception as e:
#         print(f"Not stop e : {e}")
#     finally:
#         print("Not close every time,output")
 
# PRACTICE SET------->

# Answer 1------------------------>

# f1 = ["1.txt", "2.txt", "3.txt"]
# for file in f1:
#     try:
#         f2=open(file, "r")
#         print(file,)
#         f2.close()
#     except:
#         print(file,"is not present")    

# # Answer 2---------->

# num = [10,20,30,40,50,60,70,80,90]
# for index, number in enumerate(num):
#     if index == 2 or index == 4 or index == 6:
#         print(number)

# Answer 3----------------------->

# num = int(input("enter a number: "))
# table=[num * i for i in range (1,11)]
# print(table)

# Answer 4------------------------->

# a = int(input("enter a first number: "))
# b = int(input("enter a sec number: "))
# try:
#     print("result=",a/b)
# except ZeroDivisionError:
#     print("infinite")

# Answer 5------------------------------>
# def openRead(filename):
#     try:
#         with open(filename,"r") as f:
#             print(f.read)



# num = int(inpu





# t("enter a number: "))
# table=[num * i for i in range (1,11)]
# print(table)
# with open("Table.txt","a")as f:
#     f.write(f"\n {table}")

# MAP FUNCTION------------------->


# numbers = [1, 2, 3]
# def mul_1(num):
#     return num * 2
# double = map(mul_1, numbers)
# print(list(double))

# fruit=["apple","mango"]
# stri_f=" and ".join(fruit)
# print(stri_f)