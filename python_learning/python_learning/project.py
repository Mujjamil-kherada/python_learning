# class transport():
#     def __init__(self,name,kg,mal):
#         self.name=name
#         self.kg=kg
#         self.mal=mal
#     def samaan(self):
#         if self.kg < 10000 :
#             print(f'dap loded to tampo :{self.name}')
#         elif self.kg > 10000:
#             print(f'over loding in tampo: {self.name}')
#             print('gover ment reuls breke')
#             print(f"*"*30)
#     def enter(self):
#         if self.kg < 10000:
#             print(f'dap is transpport {self.kg} kg and {self.mal} to modasa to market')
#         if self.kg > 10000:
#             print(f' {self.kg}  dap stor a godown')
#             print(f"*"*30)
#     def show(self):
#         print(f'mal {self.mal}stor to godowen')
#     def count(self):
#         print(f'kul totale 80 boni is {self.mal}')
#         print(f"*"*30)
#     def plus(self):
#         for i in range(1):
#             self.mal = i
#             print(f'samman stord in {i} godaune ')
#             print('mal stord ho gya he')
#             print(f"*"*30)
        
        

            
# tampo=transport('asoke lelon',5000,'dap product')
# tampo.samaan()
# tampo.enter()
# tampo.show()
# tampo.count()
# tampo.plus()    
     
# class student():
#     def __init__(self,fname,lname):
#         self.fname=fname
#         self.lname=lname
#     @property
#     def email(self):
#       return  self.fname + self.lname + '@gmail' + '.com '
#     @change_ satter

# me=student('mujjamil','kherada')
# print(me.email)
class hi():
    def __init__(self,name,tiket_class,tiket_vip):
        self.name=name
        self.tiket_class=tiket_class
        self.tiket_vip=tiket_vip
    def chaking(self):
        if self.tiket_class <10:
            print('yes you tiket is normel class')
        if self.tiket_vip >10 :
            print('yes is vip class')
class by(hi):
    def __init__(self,name,last):
        self.name=name
        self.last=last
    def dastinastion(self):
        print(f'you are stop sir happye jarny {self.name} ')
        print(f'pless giv yor rivyou {self.last}')

bus=hi('kasib',3,18)
bus2=hi('mohib',15,4)
bus.chaking()
bus2.chaking()
by1=by('kasib','10')
by1.dastinastion()


