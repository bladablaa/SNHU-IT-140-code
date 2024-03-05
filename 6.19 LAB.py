

word_replacements = input().split()

word_pairs = {}                                   # store the new words in a dicionary
for i in range(0, len(word_replacements), 2):
    original_word = word_replacements[i]
    new_word = word_replacements[i + 1]
    word_pairs[original_word] = new_word


sentence = input()                                  #set the second input to a variable


words = sentence.split()                            #split the sentence into words and
for word in words:                                  #check if each word needs to be replaced
    if word in word_pairs:
        print(word_pairs[word], end = ' ')
    else:
        print(word, end= ' ')
