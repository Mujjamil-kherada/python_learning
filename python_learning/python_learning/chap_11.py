# que--What is dimond problem

# what is super mathod

# class Animal:
#     def Legs(self):
#         print("Animals have four legs")

#     def Food(self):
#         print("Animals eats grass and meat")

# class cat(Animal):
#     def Eyes(self):
#         print("cat have two eyes")
    
# class Dog(Animal):
#     def bark(self):
#         print("Bhow bhow")

# class Cow(Animal):
#     def nose(self):
#         print("cow has one nose")

#     def tail(self):
#         print("Cow has one tail")

# class Lion(Animal):
#     def king(self):
#         print("Lion is king of forest")

#     def run(self):
#         print("Lion runs fast")

# class leopard(Animal):
#     def fast(self):
#         print("leapord is fastest Animal in the world")

#     def eat(self):
#         print("leopord eats other animal like buffelo,dear,Etc..")

# class Tiger(Animal):
#     def national(self):
#         print("Tiger is national animal of india")

#     def called(self):
#         print("Tiger called big cat in world")

# simba=Dog()
# simba.Legs()
# simba.bark()
# simba.Food()

# mini=cat()
# mini.Eyes()

# Cow=Cow()
# Cow.nose()
# Cow.tail()

# Lion=Lion()
# Lion.king()
# Lion.run()

# leopard=leopard()
# leopard.fast()
# leopard.eat()

# Tiger=Tiger()
# Tiger.called()
# Tiger.national()


# class Employee:
#     def __init__(self,salary,bonus):
#         self.salary=salary
#         self.bouns=bonus
#     @property
#     def in_hand(self):
#         return self.salary+self.bouns
    
#     @in_hand.setter
#     def bonus(self,C_salary):
#         self.bonus=C_salary-self.salary

# haidar=Employee(1000,200)
# print(haidar.bonus)
# print(haidar.in_hand)
# # haidar.in_hand=1500
# print(haidar.bonus)


# class Student:
#     def __init__(self,First_name,Last_name):
#         self.First_name=First_name
#         self.Last_name=Last_name
#     @property
#     def mail_name(self):
#         return self.First_name+self.Last_name +"@gmail"+".com"
#     # @change_ satter
    
# mail= Student("mohib","kherada2880")
# print(mail.mail_name)
    
# # Syntax
# class Employee:
#     pass
# class programmer(Employee):
#     pass

# Types of inheritance------>

# 1-->Single inheri...

# class Animal:
#     def eat(self):
#         print("Animal eats grass")

# class dog(Animal):
#     pass
# Animal=dog()
# Animal.eat()

# # 2---->Multiple inher...

# class Animal:
#     def eat(self):
# #         print("Animal eats grass")

# class run:
#     def play(self):
#         print(" Animal runs fast")

# class Dog(Animal, run):
#     pass
# d = Dog()
# d.eat()
# d.play()

# 3--->multivle inheri...

# class Animal:
#     def eat(self):
#         print("Animal eats grass")

# class dog(Animal):
#     def drink(self):
#         print("Animal drinks water")

# class pet(dog):
#     pass
# Animal=pet()
# Animal.drink()
# Animal.eat()

