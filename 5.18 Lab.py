def exact_change(input_val):
    """if input != 0, calculates the number of each type of change"""
    new_total = input_val
    if input_val <= 0:
        print('no change')
    if new_total >= 100:
        num_dollars = new_total // 100
        new_total -= num_dollars * 100
    else:
        num_dollars = 0
    if new_total >= 25:
        num_quarters = new_total // 25
        new_total -= num_quarters *25
    else:
        num_quarters = 0
    if new_total >= 10:
        num_dimes = new_total // 10
        new_total -= num_dimes * 10
    else:
        num_dimes = 0
    if new_total >= 5:
        num_nickels = new_total //5
        new_total -= num_nickels *5
    else:
        num_nickels = 0
    if new_total >= 1:
        num_pennies = new_total
    else:
        num_pennies = 0
    return num_dollars, num_quarters, num_dimes, num_nickels, num_pennies

def num_of_change(num_dollars, num_quarters, num_dimes, num_nickels, num_pennies):
    """Prints if the change type needs to print, and checks if it should print plural"""
    if num_dollars == 1:
        print(num_dollars, 'dollar')
    elif num_quarters >= 2:
        print(num_dollars, 'dollars')

    if num_quarters == 1:
        print(num_quarters, 'quarter')
    elif num_quarters >= 2:
        print(num_quarters, 'quarters')

    if num_dimes == 1:
        print(num_dimes, 'dime')
    elif num_dimes >= 2:
        print(num_dimes, 'dimes')

    if num_nickels == 1:
        print(num_nickels, 'nickel')
    elif num_nickels >= 2:
        print(num_nickels, 'nickels')

    if num_pennies == 1 :
        print(num_pennies, 'penny')
    elif num_pennies >= 2:
        print(num_pennies, 'pennies')

if __name__ == '__main__':
    input_val = int(input())
    # sets variables based on output of exact_change function
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val)
    #runs those variables throught the num_of_change function
    num_of_change(num_dollars, num_quarters, num_dimes, num_nickels, num_pennies)
