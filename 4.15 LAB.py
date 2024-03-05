word = input()
password = ''

for i in word:                 #Check each character in the input password
    if i == 'i':               #If the character is'i' 'a' 'm' 'b' or 'o'
        password += '!'        #replace them with their coresponding character
    elif i == 'a':
        password += '@'
    elif i == 'm':
        password += 'M'
    elif i == 'B':
        password += '8'
    elif i == 'o':
        password += '.'
    else:                      #if the character is anything else, keep it as is
        password += i
password += 'q*s'              #add 'q*s' to the end
print(password)