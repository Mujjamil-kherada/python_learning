age=13
if age >18 :
    print('valid')
elif age >12 and age <18:
    print('ten')
else:
    print('kids')
# 6 prectise set in if ,elif,else
# Q,1
a=int(input('enter number:'))
if a > 50:
    print('big number')
elif a > 20 and a <50 :
    print('mid number')
else: 
    print('smoll number') 

# Q,2
a=int(input('enter mark :'))
b=int(input('enter mark :'))
c=int(input('enter mark :'))
d=[a,b,c]
ave=sum(d)
if ave > 40 :
    print(f'exilent,{ave}:')
elif ave > 30 and ave < 40:
    print(f'very good,{ave}:')
else:
    print(f'file,{ave}:')

# Q,3

taxt=input('enter the taxt:')
if 'make a lot mony' in taxt:
    print('spam')
elif 'buy now' in taxt or 'subscribe this'in taxt or 'clike this'in taxt:
    print('spam')
else:
    print('not spam')

taxt=input('enyer taxt:')
if 'school' in taxt:
    print('ok')
elif 'home' in taxt or 'parke' in taxt:
    print('noproblam')
else:
    print('not go')

# q,4

taxt=input('enter taxt:')
if len(taxt) < 10 :
    print('valide')
else:
    print('not valid')


# q,5

name=['harun','sani','zib','mohin','ikan']
find=input('find name:')

if find in name:
    print('yese')
else:
    print('no')

# Q,6

marks=int(input('enter marks:'))
if marks >= 90:
    print('exilent')
elif marks >= 85:
    print('vary good')
elif marks >= 75:
    print('good')
elif marks >= 65:
    print('nice')
elif marks >= 55:
    print('ave')
else:
    print('file')