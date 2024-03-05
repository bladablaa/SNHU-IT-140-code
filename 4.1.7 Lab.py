

word = ''
num = ''
other = ''

my_dict = {}

while True:                                          #start a loop
    string = input('Enter a word and a number:')     #prompt for input

    for i in range(len(string)):                    #Check every character the input string
        if string[i].isdigit():                     #if its a digit, assign it to the variable 'num'
            num += string[i]
        elif string[i].isalpha():                   #if its an alphabetical character, assign it to variable 'word'
            word += string[i]
        else:                                       # if its anything else, assign it to 'other' as a place holder
            other += string[i]
    if word == 'quit':                              # if the 'word' is quit, stop loop
        break
    my_dict[num] = word                             # add the number and word pair to the dictionary
    word = ''                                       #clear the values for the next loop
    num = ''
    other = ''

for n, w in my_dict.items():                        #for all the pairs in the dictionary, print the sentence
    print(n, w, 'is far too many!')

