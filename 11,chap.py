


11_prectise
Q=1

class c2dvector():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return (f'{self.x},{self.y}')

class c3dvector(c2dvector):
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __str__(self):
         return (f'{self.x},{self.y},{self.z}')

A=c2dvector(1,2)
print('c2dvector:',A)
B=c3dvector(1,2,3)
print('c3dvector:',B)

Q=2

class Animel():
    def body_parts(self):
        print('animel has a body stretcher difrent humans')
    def living(self):
        print('animel living in forest and mountent humans arya')
class cat(Animel):
    def pet(self):
        print('cat is a pet and home and humans arya living')
    def fod(self):
        print('cat fod is : (milk)(mete)(fish)(cat fod)')
class dog(cat):
    def loyel(self):
        print('dog is humans bast frend and loyel')
    def protect(self):
        print('dog is protect table Animel')

class cemal(dog):
    def memal(self):
        print('cemal is desert animel and travel animel')
    def fod(self):
        print('cemal is a mor water pr 100 litter stord and food grass,leaves eat')

class hours(cemal):
    def run(self):
        print('hours used to travel and rase most frendly to humans')
    def loks(self):
        print('hours is buttiful and focus animel')

class tiger(hours):
    def carnival(self):
        print('this is a most dangers animel and most populer animel')
    def atteker(self):
        print('tis is hunt another animel bear ,cow,another speciality is living allon ')


class wolf(tiger):
    def winter(self):
        print('wolf is dep forest and most intelligent and grop atteker')
    def hunt(self):
        print('wolf grop atteker and this a bear,rabit anothe memal hunt ')

class cow(wolf):
    def milk(self):
        print('cow is a human frndly and silent memal')
    def farmar(self):
        print('cow is bast in farming and bissnes and anothe milk product this humans big banifit')

class rabit(cow):
    def fast(self):
        print('rabit is fast and flcsibel memal and under ground smoll hole living  and grass around')
    def eat(self):
        print('rabit is a hunter by killing and another animel killed this a live human fod')

class ret(rabit):
    def smoll(self):
        print('ret is smoll and living in woll hole in human arya ')
    def eat(self):
        print('ret eat seed and roti a insect')

Animel=Animel()
Animel.body_parts()
Animel.living()

cat=cat()
cat.pet()
cat.fod()

dog=dog()
dog.loyel()
dog.protect()

cemal=cemal()
cemal.memal()
cemal.fod()

hours=hours()
hours.run()
hours.loks()

tiger=tiger()
tiger.carnival()
tiger.atteker()

wolf=wolf()
wolf.winter()
wolf.hunt()

cow=cow()
cow.milk()
cow.farmar()

rabit=rabit()
rabit.fast()
rabit.eat()

ret=ret()
ret.smoll()
ret.eat()

Q=3

class employee():
    def __init__(self,salary,bonus):
        self.salary=salary
        self.bouns=bonus
    @property
    def in_hand(self):
        return self.salary +self.bouns

    @in_hand.setter
    def in_hand(self,c_salary):
        self.bouns=c_salary-self.salary

mujjamil=employee(1000,200)
print(mujjamil.in_hand)
mujjamil.in_hand=1500
print(mujjamil.in_hand)

Q=4

class complex():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self, number):
        return complex(self.x + number.x,self.y + number.y)
    def __mul__(self,number):
        x_1 = self.x * number.x - self.y * number .y
        y_2 =  self.x * number.y + self.y * number .x
        return complex(x_1,y_2)
    def __str__(self):
        if self.x > 0:
            return (f'{self.x}+{self.y}')
        else:
            return (f'{self.x}{self.y}')
ob_1=complex(2,3)
ob_2=complex(1,4)

print('ob_1:',ob_1)
print('ob_2:',ob_2)
print('ob_1 + ob_2',ob_1 + ob_2)
print('ob_1 * ob_2',ob_1 * ob_2)

Q=5

class vactor():
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __add__(self,kyebi):
        return vactor(self.x + kyebi.x , self.y + kyebi.y , self.z + kyebi .z)
    def __mul__(self,kyebi):
        return self.x * kyebi.x + self.y * kyebi.y + self.z * kyebi .z
    def __str__(self):
        return (f'{self.x},{self.y},{self.z}')
v_1=vactor(1,2,3)
v_2=vactor(4,5,6)

print('v_1:',v_1)
print('v_2:',v_2)
print('v_1 + v_2:',v_1 + v_2)
print('v_1 * v_2:',v_1 * v_2)

Q=6

class vactor():
    def __init__(self,x,y,z,):
        self.x=x
        self.y=y
        self.z=z
    def __str__(self):
        return (f'{self.x}j{self.y}i{self.z}k')
v_1=vactor(7,8,10)
print(v_1)

Q=7
class focus ():
    def __init__(self,name,sarname,adress):
        self.name=name
        self.sarname=sarname
        self.adress=adress
    def box(self):
        return (f'{self.name} {self.sarname} {self.adress}')
    def __len__(self):
        return 3

v_1=focus('muujjamil','kherada','modasa')
print(v_1)
print(len(v_1))

class t2():
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __add__(self,number):
        return (self.x + number .x ,self.y + number .y + self.z + number.z )
    def __mul__(self,number):
        return self.x * number.x + self.y* number .y + self .z* number.z
    def __str__(self):
        return (f'{self.x},{self.y},{self.z}')
v1=t2(2,3,4)
v2=t2(5,6,7)
print('v1:',v1)