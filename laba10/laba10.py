import random
import string
winner = ""
max_score = 0
with open('file41.txt', 'r', encoding='utf8') as file:
    record = file.readline()
    while record:
        human = record.split()
        if int(human[-1]) > max_score:
            second_place=winner
            second_score=max_score
            winner = human[0] + " " + human[1]
            max_score = int(human[-1])
            
        record = file.readline()
print("Призер:", second_place, " ( Набранное количество баллов:", second_score, ')')
print("========")
def finder(filename):
    with open(filename, 'r', encoding='utf8') as file:
        record = file.readline()
        while record:
            if " Academy" in record:
                return True
            record = file.readline()
if finder("file5.txt"):
    print("В 5 файле")
elif finder("file6.txt"):
    print("В 6 файле")
print("========")
e_counter=0
e_words=[]
all_words=0
with open('file6.txt', 'r', encoding='utf8') as file:
        record = file.readline()
        while record:
            splited=record.split()
            all_words+=len(splited)
            for word in splited:
                for e_finder in word:
                     if e_finder=='e':
                            e_counter+=1
                            e_words.append(word)
            record = file.readline()
print(*e_words)
print("Всего слов - ", all_words)
print("Слов с буквой e - ", e_counter)
print("Итого % слов с буквой e - ", (e_counter/all_words)*100,"%")
print("========")
def file_opener(filename):
    with open(filename, 'r', encoding='utf8') as file:
        for i in range(n):
            record = file.readline()
            if record:
                human = record.split()
                print(*human[0])
            else:
                print("В файле нет больше данных")
                break
            
n=int(input("Введите количество имен: "))
pol=input("Введите пол (М/Ж): ")
if pol.lower() == "м":
    file_opener("file8.txt")
if pol.lower() == "ж":
    file_opener("file7.txt")
print("========")
def add_line_to_middle(filename, new_line):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    middle_index = len(lines) // 2
    lines.insert(middle_index, new_line + '\n')
    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines(lines)

new_line = input("Введите строку для добавления в середину файла: ")

add_line_to_middle("file4.txt", new_line)
print("========")
processed_lines=[]
def reverse_words_in_file(input_filename, output_filename):

    with open(input_filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    for line in lines:
        words = line.split()
        reversed_words = [word[::-1] for word in words]
        processed_line = ' '.join(reversed_words)
        processed_lines.append(processed_line)
    with open(output_filename, 'w', encoding='utf-8') as file:
        file.write('\n'.join(processed_lines))
filename=input("Введите название файла")
reverse_words_in_file(filename, "new_file.txt")
print("========")
valid_words=[]
punctuation="!@#$%^&*()_+?>./,;:[]}{\""
def generate_password(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                words=line.split(" ")
                for word in words:
                     for p in punctuation:
                          if p in word:
                               word=word.replace(p,'')
                     word.translate(str.maketrans('', '', string.punctuation))
                     if len(word)>=3:
                          valid_words.append(word)
        if len(valid_words) < 2:
            print("Недостаточно подходящих слов для создания пароля.")
        for _ in range(100):
            word1, word2 = random.sample(valid_words, 2)
            password = word1.capitalize() + word2.capitalize()
            if 8 <= len(password) <= 10:
                print(f"Сгенерированный пароль: {password}")
                return
        
file_path = input("Введите название файла для генерации: ")

generate_password(file_path)
print("========")
n, m = map(int, input().split())
for i in range(1, n + 1):
    if i % 2 == 1:
        print('#' * m)
    else:
        if (i // 2) % 2 == 1:
            print('.' * (m - 1) + '#')
        else:
            print('#' + '.' * (m - 1))
