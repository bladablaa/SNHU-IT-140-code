
#x=15
#print('{x:*<10.3f}'.format(x=6))

#print('{x:#^10.2f}'.format(x=x))

##phrases = ['To be, ', 'or not to be.\n', 'That is the question.']

##sentence = ''
##for phrase in phrases:
    ##sentence += phrase
##print(sentence)

name = input('What is your name? \n')
age = int(input('How old are you?\n'))

from datetime import date
current_yr = date.today().year

birth_year = current_yr - age

print('Hello', name, '. You were born in', str(birth_year) + '.')

