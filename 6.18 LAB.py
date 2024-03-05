user_input = input()

count = {}

for word in user_input.split():                 #loop throught the input and add one to the value
                                                #of the key for that word
    count[word] = count.get(word, 0) + 1

for word in user_input.split():                 #then loop through the input printing the final value with each key
    print(word, count[word])