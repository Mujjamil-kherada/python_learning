# class Air_line():
#     def __init__(self,name,thiket_boking):
#         self.name=name
#         self.thiket_boking=thiket_boking
#     def info(self):
#         print(f'sir this is s  {self.name}')
#         print(f'yuor  thiket number is {self.thiket_boking}')
#         print(f'thankx four boking to {self.name}')

#         print(f"*"*30)
        
# class Air_pote(Air_line):
#     def __init__(self,cabine_crow,thiket,passenger,set_class):
#         self.cabine_crow=cabine_crow
#         self.thiket=thiket
#         self.passenger=passenger
#         self.set_class=set_class
#     def chaking(self):
#         print(f'sir i am  {self.cabine_crow} pless chaking you thiket sir')
#         print(f'yes sir your set num is {self.thiket}')
#         print(f'ok thankyou{self.passenger}')
#         print(f'sir yor set is {self.thiket} and your class is {self.set_class}')
#         print(f"*"*30)
# class Air_plen(Air_pote):
#     def __init__(self,travel,dastination,rest,time):
#         self.travel=travel
#         self.dastination=dastination
#         self.rest=rest
#         self.time=time
#     def yatra(self):
#         print(f'travel to {self.travel} to {self.dastination} mid mornig ste {self.rest} araund Air mark {self.time} four {self.dastination}')
#         print(f"*"*50)
# class Air_inside(Air_plen):
#     def __init__(self,set_number,lunce):
#         self.set_number=set_number
#         self.lunce=lunce
#     def set_1(self):
#         print(f'sir thre is your set sir pless set down sir set numbner is {self.set_number}')
#         print(f'set number {self.set_number}  four lunce time hu is lunce {self.lunce}')
#         print(f'*'*30)
# class Air_rest(Air_inside):
#     def __init__(self,rest,time,niklo):
#         self.rest=rest
#         self.time=time
#         self.niklo=niklo
#     def go(self):
#         print(f'sir ste in {self.rest} fule')
#         print(f'rest time is {self.time} and going to {self.niklo}')




        
# indigo=Air_line('Indigo Air line','A45')
# Air_line.info(indigo)
# indigo=Air_pote('sima cabine crow','A45','kasib','normal class')
# Air_pote.chaking(indigo)
# indigo=Air_plen('ahemdabad','londan','delhi','5 hours')
# Air_plen.yatra(indigo)
# indigo=Air_inside('A45','pasta')
# Air_inside.set_1(indigo)
# indigo=Air_rest('delhi','30 min','londan')
        

       
# class school():
#     def __init__(self,name,address,contact):
#         self.name=name
#         self.address=address
#         self.contact=contact
#     def box(self):
#         print(f'school name is {self.name}')
#         print(f'address {self.address}')
#         print(f'contact number{self.contact}')
#         print(f'_'*70)
# class school_study(school):
#     def __init__(self,name,subject):
#         self.name=name
#         self.subject=subject
#     def box_2(self):
#         print(f'{self.name} subject is :{self.subject} ')
#         print(f'_'*70)
# class school_student_bench(school_study):
#     def __init__(self,bench,student,time_class):
#         self.bench=bench
#         self.student=student
#         self.time_class=time_class
#     def open(self):
#         if self.bench < 20:
#             print(f'class is a {self.bench} four student')
#         elif self.student < 40:
#             print(f'yes class is full and all student is available:{self.student}')
#         elif self.student < 15:
#             print(f'class is not full addmision is start four student now {self.student} ')
#             print(f'_'*70)
#     def max(self):
#         print(f'admission is full and class is start tomorrow')
#         print(f'class time is 10 :30 to 1:30')
    
#         if self.time_class < '10:30':
#             print(f'yes allow go to class')
#         elif self.time_class > '10:30':
#             print(f'is not allow in  class')
#         else:
#             print(f'10:30 bord line case')
#         print(f'_'*70)
        
    
     


# school_1=school('lg school english and gujarati medium','iti Area modasa','9907458364')
# school_1.address=('baruna rod in modasa')
# school.box(school_1)
# school_1=school_study('class_10',['mats','histry','english','gujarati'])
# school_study.box_2(school_1)
# school_1=school_student_bench(20,40,'10:34')
# school_1.open()
# school_1.max()

# class shnkiya():
#     count=0
#     def __init__(self,name,count_student):
#         self.name=name
#         self.count_student=count_student
#     def box(self):
#         if self.count_student :
#             print(f'prestion {self.name}')
#         else:
#             print('appstion')
    
#     def box2(self):
#         if self.count_student:
#             print(f'totel appstion student is {self.count_student}')
        
# student1=shnkiya('rahul',['mohib','sani','ayan'])
# student2=shnkiya('mujjamil',['soeb','kasib'])
# print('kon',shnkiya.count)

    

