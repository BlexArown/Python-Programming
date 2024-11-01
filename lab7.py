text = input("Введите текст:\n").split(" ")
print(text)
for i in range (len(text)-1):
    if text[i] == text[i+1]: text[i+1]=""
print(*text)


text = input("Введите фразу:\n").split(" ")
if len(text)==2:
    print(*text[::-1])
else:
    print("Ошибка!")

    
text = input("Введите слово:\n")
text=[a+"." for a in text]
text=' '.join(text)
print(text[0:-1])


def correct(review):
    review = review.replace("не плохой", "хороший")
    review = review.replace("не плоха", "хороша")
    return review
def main():
    print("Введите ваши отзывы (введите 'стоп' для завершения):")
    while True:
        review = input("Отзыв: ")
        if review.lower() == 'стоп':
            break
        corrected = correct(review)
        print(f"Исправленный отзыв: {corrected}\n")
print(main())

gl="аеёиоуэюя"
i = input("Введите текст:\n")
i=i.split("/")
counter=0
m=[]
for k in i:
    for n in range(len(k)):
        if k[n].lower() in gl:
            counter+=1
    m.append(counter)
    counter=0
if m==[5,7,5]: print("Хайку!")
else:
    if len(i)!=3:
        print("Не хайку. Должно быть 3 строки.")
    else:
        print("Не хайку.")

msg = input("Введите зашифрованное сообщение:\n ")
ans = msg[0:-1:2]+msg[1:-1:2][::-1]
if (msg[-1]=="#") and (msg[:-2].isalpha()):
    print("Дешифрованное сообщение:", ans)
else:
    print("Ошибка! Отсутствует символ #")

import random
options=[]
upLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowLetters=upLetters.lower()
digits="0123456789"
SpS="!@#$%^&*_-+="
length = int(input("Введите длину пароля:\n"))
options.append(input("Нужны заглавные буквы? y/n:\n"))
options.append(input("Нужны строчные буквы? y/n:\n"))
options.append(input("Нужны цифры? y/n:\n"))
options.append(input("Нужны спец.символы? y/n:\n"))
password =""
for x in range(len(options)):
    if options[x].lower() in ["y","yes"]:
        options[x]=1
    else:
        options[x]=0
total= upLetters*options[0]+lowLetters*options[1]+digits*options[2]+SpS*options[3]
for i in range(length):
    password += random.choice(total)
print(password)


i = input("Введите результат матча:\n")
a=i.split("-")[0]
b=i.split("-")[1]
score =b.split(" ")[1]
b=b.replace(score,"")
if score.split(":")[0]>score.split(":")[1]:
    print(a)
else:
    if score.split(":")[0]==score.split(":")[1]:
        print("Ничья")
    else:
        print(b)
