

user_text = input()

length=len(user_text)
for i in range(length):
    if user_text[i] == ' ':
        length -= 1
    if user_text[i] == '.':
        length -= 1
    if user_text[i] == ',':
        length -= 1

print(length)