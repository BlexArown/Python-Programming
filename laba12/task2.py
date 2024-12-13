messages_count = int(input("Введите количество вопросов: "))
message_queue = []
messages = ""

if not messages_count:
    print("Сообщений не найдено.")
    exit()
else:
    messages = input("Введите ответы и не ответы: ")[:messages_count]

# This works assuming the messages consist only of "Q" and "A"
for message in messages:
    if message == "Q":
        message_queue.append("Q")
    elif len(message_queue) > 0:
        message_queue.pop(0)
    else:
        print("-")
        break
else:       
    if len(message_queue) > 0:
        print("-")
    else:
        print("+")
