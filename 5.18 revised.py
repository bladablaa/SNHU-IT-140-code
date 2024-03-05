#
# def exact_change(input_val):
#     coins = {'dollars': 100, 'quarters': 25, 'dimes': 10, 'nickels': 5, 'pennies': 1}
#                                                 #create dictionary of coins
#     change = {}                                 #create an empty dictionary where the number of each coin
#     if input_val <= 0:
#         return None
#                                                 #needed will go
#     for name, value in coins.items():           #loop over the input value for each denomination
#         if input_val >= value:
#             num_coins = input_val // value      #check how many coins can go into input value
#             input_val %= value                  #iterate input value for remainder
#             change[name] = num_coins            #add the number of coins to the change list
#         else:
#             change[name] = 0                    #if the denomination can not fit in the input value, set it to 0
#     return change
#
# def num_change(change):                         #print function checking for no print/multiple coins
#     if change is None:
#         print("no change")
#     else:
#         for name, num_coins in change.items():      #loop over each pair in change dictionary
#             if num_coins == 1:                  #if a single coin
#                 print(f"{num_coins} {name[:-1]if name != 'pennies' else 'penny'}")
#                                                 #remove the last letter,
#                                                 #but if its pennies, replace with penny
#             elif num_coins >=2 :                #if its 2 or more otherwise print the predefinied name
#                 print(f"{num_coins} {name}")
#
# if __name__ == '__main__':
#     input_val = int(input())
#     change = exact_change(input_val)            #define change as the outputs of exact_change
#     num_change(change)                          #run change throught num_function

# def exact_change(input_val):
#         denominations = {'dollars': 100, 'quarters': 25, 'dimes': 10, 'nickels': 5, 'pennies': 1}
#         change = {}
#
#         for name, value in denominations.items():
#             if input_val >= value:
#                 num_coins = input_val // value
#                 input_val %= value
#                 change[name] = num_coins
#             else:
#                 change[name] = 0
#
#         return change
#
#
# def num_of_change(change):
#     for name, num_coins in change.items():
#         if num_coins != 0:
#             if num_coins == 1:
#                 print(f"{num_coins} {name[:-1]if name != 'pennies' else 'penny'}")
#             else:
#                 print(f"{num_coins} {name}")
#
#
# if __name__ == '__main__':
#     input_val = int(input("Enter the amount in cents: "))
#     change = exact_change(input_val)
#     num_of_change(change)

def exact_change(input_val):
    coins = {'dollars': 100, 'quarters': 25, 'dimes': 10, 'nickels': 5, 'pennies': 1}
    change = {}

    if input_val <= 0:
        return None

    for name, value in coins.items():
        if input_val >= value:
            num_coins = input_val // value
            input_val %= value
            change[name] = num_coins
        else:
            change[name] = 0

    return list(change.values())  # Return only the values (coin counts)

def num_change(change):
    if change is None:
        print("no change")
    else:
        for count in change:  # Iterate over the coin counts
            print(count)

if __name__ == '__main__':
    input_val = int(input("Enter the amount in cents: "))
    change = exact_change(input_val)
    num_change(change)

# If you want to print only the numbers, you can use the print function like this:
print(*exact_change(300))
