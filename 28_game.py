# import random
# print("computer choos a game: roke(r),papar(p),sizhaer(s)")
# com=(random.randint(1, 3))
# if com==1:
#     print('r')
# if com==2:
#     print('p')
# if com==3:
#     print('s')

# you=input("you choos a game:roke(r),papar(p),sizhaer(s) ")

# def woh_wine(com,you):

#     if com==you:
#        return None

#     elif com=='r':
#         if you=='s':
#             return True

#     elif com=='s':
#         if you=='p':
#             return True

#     elif com=='p':
#         if you=='r':
#             return True

#     elif com=='p':
#         if you=='k':
#             return False

#     elif com=='r':
#         if you=='k':
#             return False

#     elif com=='s':
#         if you=='roke':
#             return False

# result = woh_wine(com,you)

# if result:
#     print(f'you wine {com}congress ')
# elif result is None:
#     print('drew')
# else:
#     print(f'you loose in {com}')    

import random
print ('computer choos : roke(r),papare(p),katar(k)')
com=(random.randint(1, 3))
if com==1:
    
    
if com==2:
    print('p')
if com==3:
    print('k')
you=input('you choos : roke(r),papare(p),katar(k)')

def woh_wine(com,you):

    if com==you:
       return None

    elif com=='r':
        if you=='p':
          return True

    elif com=='p':
        if you=='k':
          return True

    elif com=='k':
        if you=='r':
          return True

    elif com=='r':
        if you=='p':
          return False

    elif com=='p':
        if you=='k':
          return False

    elif com=='k':
       if you=='r':
          return False

result=(woh_wine(com,you))
if result:
    print(f'you wine congress{com}')
elif  result :
    print ('drew')
else:
    print(f'you loos this mache {com}')
