# class Bank():
#     def widreow(self):
#         pass
#     def check_balance(self):
#         pass
#     def deposit(p):
#         print("paisa apo")

# HDFC=Bank()
# axis=Bank()
# print(HDFC.deposit())

#  class student():
#     def __init__(self,name,lang):
#         self.name=name
#         self.lang=lang
#     def get_info(self):
#         print(f"Student name is {self.name}, and its learning the {self.lang} language")

# Ayan=student("Ayan","Python")
# Ayan.get_info()

# class teacher():
#     def __init__(self,teacher,salary):
#         self.teacher=teacher
#         self.salary=salary
#     def get_salary(self):
#         print(f"teacher name is {self.teacher}, and salary is{self.salary}")
# Haidar=teacher("Haidar","salary")
# Haidar.get_salary()

# ans-1 ------------------->

# class Programmer:
#     company = "microsoft"
#     def __init__(self,name,product):
#         self.name=name
#         self.product=product
#     def get_info(self):
#         print(f"Student name is {self.name}, and its working on {self.product} product")

# pr1=Programmer("Mujjamil","Edge")
# pr2=Programmer("Mohib","teams")
# pr3=Programmer("Ayan","vs code")
# pr4=Programmer("Sami","python")

# pr3.get_info()
# pr4.company = "Google"

# ans 2 and 4------------------------>


# class Calculator():
#     @staticmethod
#     def greet():
#         print("Hy,Mohib")

#     def square(self,num):
#         print("Square=",num*num)

#     def cube(self,num):
#         print("Cube=",num*num*num)

#     def square_root(self,num):
#         print("Square Root=",num**0.5)
# Ans= Calculator()

# Ans.greet()
# Ans.square(10)
# Ans.cube(10)
# Ans.square_root(100)

# ans 3---------------->

# ans 5---------------->

# class Train:
#     def __init__(self,name,fare,seat):
#         self.name=name
#         self.fare=fare
#         self.seat=seat
#     def get_status(self):
#         print(f"The Train name is :{self.name}")
#         print(f"Avilailble Seats Are :{self.seat}")
#         print(f"*"*30)
#     def get_fare(self):
#         print(f"Ticket Price RS.{self.fare}")

#     def Book_ticket(self):
#         if self.seat>0:
#             print(f"Thanks your seat is Booked, Seat Number{self.seat}")
#             self.seat-=1
#         else:
#             print("Sorry ... Train are fully booked")
#             print(f"*"*30)
#     def cancel_Ticket(self):
#         self.seat += 1
#         print("Ticket was canceled")


#     def gr_coach(self):
#         print("genral coach is available")

#     def ac_coach(self):
#         print("AC coach is available")
    
#     def is_food(self):
#         print("Food is available in the tarin")
#         print(f"*"*30)


# vande_bhart=Train(name="Vande Bharat",fare=200,seat=10)
# vande_bhart.get_status()
# vande_bhart.get_fare()
# vande_bhart.Book_ticket()
# vande_bhart.get_status()
# vande_bhart.gr_coach()
# vande_bhart.ac_coach()
# vande_bhart.is_food()
# vande_bhart.cancel_Ticket()
