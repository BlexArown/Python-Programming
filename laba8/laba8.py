from random import randint
N = input(">").split()
A=[]
B=[]
C='1234567890'
D='!?#№@"%^:&?*(){}[]'
for i in range(len(N)):
    if N[i] not in C and N[i] not in D:
        B.append(N[i])
    if N[i] in C and N[i] not in D:
        A.append(N[i])
print("Цифры: ", *A)
print("Строки: ",*B)

A=[]
for i in range(6):
    A.append(randint(1,50))
print(*A)

N = input("Введите список чисел: ").split()
A=[]
for i in range(0,len(N)-2):
    if N[i]<N[i+1]:
        A.append(N[i+1])
print(*A)

N = []
minn=[]
maxx=[]
ravn=[]
in_N=int(input("Введите числа: "))
N.append(in_N)
while in_N!="":
    in_N = input("Введите числа: ")
    if in_N.isdigit():
        N.append(int(in_N))
print("Введённые числа: ", *N)
avg = sum(N)/len(N)
for i in range(len(N)):
    if N[i]<avg:
        minn.append(N[i])
    if N[i]>avg:
        maxx.append(N[i])
    if N[i]==avg:
        ravn.append(N[i])
print(avg)
print(*minn)
if len(ravn)==0:
    N
else:
    print(*ravn)
print(*maxx)

N = int(input("Введите число X, рост Андрея: "))
A = []
AB = int(input("Введите рост человека: "))
if AB<=230 and AB>100:
    A.append(AB)
else:
    print("Число не подходит по правилам, его ввод отменён.")
while AB!="":
    AB = input("Введите рост человека: ")
    if AB =="":
        break
    if int(AB)<=230 and int(AB)>100:
        if AB.isdigit():
            A.append(int(AB))
    else:
        print("Число не подходит по правилам, его ввод отменён.")
A=sorted(A)
A=A[::-1]
print("Введённые числа: ", *A)
k=1
for i in range(len(A)):
    if A[i]>N:
        k+=1
    if A[i]==N:
        k+=1
    if A[i]<N:
        break
if k==1:
    print("Андрей выше всех, поэтому он должен быть первым.")
else:
    print("Андрей должен встать на место под номером:", k)

from random import randint
N=''
k=0
while True:
    A=randint(0,2)
    if A == 0:
        N+='О'
        k+=1
    if A == 1:
        N+='Р'
        k+=1
    if 'РРР' in N:
        for i in range(len(N)):
            print(N[i],end=' ')
        print('(попыток: ',k, ')',sep='')
        break

N = input("Введите номер карты: ")
A=0
B=0
for i in range(len(N)):
    if i%2 ==0:
        B+=(int(N[i ])*2)
    else:
        A+=int(N[i])
if B>9:
    B-=9
if (A+B)%10==0 and len(N)==16:
    print("Корректный номер.")
else:
    print("Некорректный номер.")
    
N = int(input("Введите количество комнат: "))
k=0
R=''
for i in range(N):
    R=input("Введите количество людей в комнате и её вместимость через пробел: ").split(" ")
    if int(R[1])-int(R[0])>=2:
        k+=1
print("Количество комнат, в которые могут заселиться Юра с Лёшей:",k)
