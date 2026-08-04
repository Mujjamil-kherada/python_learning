import random
print("computer choos a game: roke(r),papar(p),sizhaer(s)")
com=(random.randint(1, 3))
if com==1:
    print('r')
if com==2:
    print('p')
if com==3:
    print('s')

you=input("you choos a game:roke(r),papar(p),sizhaer(s) ")

def woh_wine(com,you):

    if com==you:
       return None

    elif com=='r':
        if you=='s':
            return True

    elif com=='s':
        if you=='p':
            return True

    elif com=='p':
        if you=='r':
            return True

    elif com=='p':
        if you=='k':
            return False

    elif com=='r':
        if you=='k':
            return False

    elif com=='s':
        if you=='roke':
            return False

result = woh_wine(com,you)

if result:
    print(f'you wine {com}congress ')
elif result is None:
    print('drew')
else:
    print(f'you loose in {com}')    
