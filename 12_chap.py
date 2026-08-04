a=int(input('enter tha vallu'))
try:
    e=a(10/5)
except Exception as e:
    print('error',e)
    print(e)
    

counter=0
def chalo():
    global counter
    counter = counter + 1
chalo()
print(counter)

try:
    num = int(input('number dalo:'))
    result = 10/num
    print('yes:',result)
except ZeroDivisionError as e:
    print('error',e)

try:
    num = int(input('enter value'))
    result = 10/num
    print('yes:',result)
except ValueError as e:
    print('error',e)

try:
    result = 10/'1'
except TypeError as e:
    print('yrs',e)

try:
    file = open('introh','r')
    ok = file.read()
    
except FileNotFoundError as e:
    print('yes',e)

try:
    result = [1,2,3]
    print(result[4])
except IndexError as e:
    print('yes',e)

try:
    name={'name':'mujjamil',
          'age':'20',
          'adr':'modasa',}
    print(name['blod'])
except KeyError as e:
    print('error',e)


while True:
    print('start')
    next_1=int(input('give me number'))
    next_2=34
    next_3=0
    try:
        next_3=next_2/next_1
    except Exception as e:
        print('error',e)
    finally:
        print('yes don',next_3)


<<<<<<< HEAD
# Q=1
=======
Q=1
>>>>>>> 85587b128129a9e4d3b701634378a29faa5d7daa

file_1 = ['text_1','text_2','text_3','text_4']
for file in file_1 :
    try:
        file_2 = open(file,'file_1','r')
        print('file is opend')
        file_2.close
    except:
        print(file,'is not work')

<<<<<<< HEAD
# Q=2 
=======
Q=2
>>>>>>> 85587b128129a9e4d3b701634378a29faa5d7daa

num = [1,2,3,4,5,6,7,8,9,10]
for index,number in enumerate(num):
    if index==2 or index == 4 or index == 8:
        print(number)

<<<<<<< HEAD
# Q=3  
=======
Q=3
>>>>>>> 85587b128129a9e4d3b701634378a29faa5d7daa

number=int(input('number:'))
tabel=[number * i for i in range(1,11)]
print(tabel,'tabel')

<<<<<<< HEAD
# Q=4        
=======
Q=4
>>>>>>> 85587b128129a9e4d3b701634378a29faa5d7daa

a=int(input('number:'))
b=int(input('number:'))
try:
    result=a/b
    print(result)
except ZeroDivisionError as e:
    print('error',e)

<<<<<<< HEAD
# Q=5
=======
Q=5
>>>>>>> 85587b128129a9e4d3b701634378a29faa5d7daa

number=int(input('number:'))
tabel=[number * i for i in range(1,11)]
print(tabel,'tabel')
print(khali)


try:
    
    print(khali)
except AttributeError as e:
    print(e)
print('ok')

number=[1,2,3,4]
def multy(num):
    return num + 5
dubel=map(multy,number)
print(list(dubel))

number=[1,2,3,4]
def add_1(num):
    index,ak =num
    if index == len(number)-1:
        return + 10
    return num
result = map(add_1,enumerate(number))
print(list(result)) 

<<<<<<< HEAD
# prob
number=[1,2,3,4,5,6]
def slice(number):
    return number % 1
=======
prob
number=[1,2,3,4,5,6]
def slice(number):
    return T-F
>>>>>>> 85587b128129a9e4d3b701634378a29faa5d7daa
dubel=filter(slice,number)
print(list(dubel))
    
import reduce
number=[1,2,3,4,5]
def mark(num):
    return num + 5
dubel=reduce(mark.numbner)
print(dubel)



