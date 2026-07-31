# prectis set 8
# # Q1
# def greter(a,b,c):
#     if a>=b or a>=c:
#         return a
#     if b>=a or b>=c:
#         return b
#     else:
#         return c
# number1=int(input('enter the number:'))
# number2=int(input('enter the number:'))
# number3=int(input('enter the number:'))

# print("Max num is: :",greter(number1,number2,number3))


# Q,2

# def calu(a):
#     return (a * 9/5) + 32
# print(calu(37))

# Q,3

# print('hallo',end=' ')
# print('wold')

# Q,4

# def ret(n):
#     if n == 0:
#         retur= 0
#     return n + ret (n - 1)
# print(ret(5))

# q,5

# def patt(n):
#     for i in range(n,0,-1):
#         print('* ' * i)
# print(patt(3))

# q,6

# def fanc(ince):
#     return ince * 2.54
# print(fanc(10))

# q.7
# def remove(list,word):
#     list.remove(word.strip())
#     return list

# my_list=['apple','mango','banana','watermaelen']
# print(remove(my_list,'mango'))

# q,8

# def table(n):
#     for i in range(1,11):
#         print(f'{n}x{i}={n*i}')
# n=int(input('enter number:'))
# table(n)