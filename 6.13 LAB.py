
list = input()                                  #gets user input

numbers = list.split()                          #splits the input into a list
numbers = [int(i) for i in numbers]             #turns each item into an integer
for i in numbers[:]:                            #creates a copy of the list to loop through
    if i < 0:                                   #if number is negative
        index = numbers.index(i)                #removes number from list i
        numbers.pop(index)
sorted_numbers = sorted(numbers)                #sorts the list

for i in sorted_numbers:                        #prints the list in plain text
    print(i, end=' ')
