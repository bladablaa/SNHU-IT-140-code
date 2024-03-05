

list = input()                              #recieve user input

numbers = [int(i) for i in list.split()]      #splits and turns input into in integers
average = sum(numbers) / len(numbers)       #calculates the average of the numbers

print(average, max(numbers))