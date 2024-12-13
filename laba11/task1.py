buttons = {
    1: [".", ",", "?", "!", ":"],
    2: ["A", "B", "C"],
    3: ["D", "E", "F"],
    4: ["G", "H", "I"],
    5: ["J", "K", "L"],
    6: ["M", "N", "O"],
    7: ["P", "Q", "R", "S"],
    8: ["T", "U", "V"],
    9: ["W", "X", "Y", "Z"],
    0: [" "]
}

inputuser = input("Введите текст: ")

result = ""
for let in inputuser.upper():
    for key in buttons.keys():
        if let in buttons[key]:
            result += str(key) * (buttons[key].index(let) + 1)
            break
print(result)
