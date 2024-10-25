import random
import string
def remove(txt):
    lines = txt.splitlines()
    corr_lines = []
    for line in lines:
        words = line.split()
        corr_words=[]
        prev_word = None
        for word in words:
            if word != prev_word:
                corr_words.append(word)
                prev_word = word
        corr_lines.append(' '.join(corr_words))
    return '\n'.join(corr_lines)
txt = """Довольно распространённая ошибка ошибка это лишний повтор повтор
слова слова Смешно не не правда ли
Не нужно портить хор хоровод"""
output_txt = remove(txt)
print(output_txt)
print("\n=============================\n\ntask2\n")
def perevorot(txt):
    words = txt.split()
    if len(words) != 2:
        return "Пожалуйста, введите фразу из двух слов."
    perevorot = f"{words[1]} {words[0]}"
    return perevorot
txt = input("Введите фразу из двух слов: ")
result = perevorot(txt)
print(result)
print("\n=============================\n\ntask3\n")
def format(txt):
    if not txt: return txt
    return '.'.join(txt)
vxod = input("Введите сообщение: ")
result = format(vxod)
print(result)
print("\n=============================\n\ntask4\n")
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
print("\n=============================\n\ntask5\n")
al="аеёиоуэюя"
i = input("Type text here:\n")
i=i.split("/")
counter=0
m=[]
for k in i:
    for n in range(len(k)):
        if k[n].lower() in al:
            counter+=1
    m.append(counter)
    counter=0
if m==[5,7,5]: print("Хайку!")
else:
    if len(i)!=3:
        print("Не хайку! Должно быть 3 строки")
    else:
        print("Не хайку!")
print("\n=============================\n\ntask6\n")
msg = input("Введите сообщение для расшифровки:\n ")
ans = msg[0:-1:2]+msg[1:-1:2][::-1]
if (msg[-1]=="#") and (msg[:-2].isalpha()):
    print("Расшифрованное сообщение:", ans)
else:
    print("Не расшифровано")
print("\n=============================\n\ntask7\n")
def generate_password(length, use_upper, use_lower, use_digits, use_special):
    characters = ""
    
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        return "Необходимо выбрать хотя бы один тип символов для генерации пароля."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Генерация пароля")
    length = int(input("Введите желаемую длину пароля: "))
    use_upper = input("Нужны ли заглавные буквы? (да/нет): ").strip().lower() == "да"
    use_lower = input("Нужны ли строчные буквы? (да/нет): ").strip().lower() == "да"
    use_digits = input("Нужны ли цифры? (да/нет): ").strip().lower() == "да"
    use_special = input("Нужны ли специальные символы? (да/нет): ").strip().lower() == "да"
    password = generate_password(length, use_upper, use_lower, use_digits, use_special)
    
    print(f"Сгенерированный пароль: {password}")
print(main())
print("\n=============================\n\ntask8\n")
i = input("Введите текст:\n")
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
    

