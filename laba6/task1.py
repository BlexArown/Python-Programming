maxx=0
minn=100000000
N=1
while N!=0:
    N=int(input("Введите рост человека: "))
    if N<minn and N!=0:
        minn = N
    if N>maxx:
        maxx = N
print("Самый высокий человек с ростом:", maxx, "\nСамый низкий человек с ростом:", minn)
N='10110'
a='0'
for i in range(len(N)-1,0,-1):
    if N[i] == '1':
        N = N + '2'**a
    a = a+'1'
print(N)
