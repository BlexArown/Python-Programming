import random
import string
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
