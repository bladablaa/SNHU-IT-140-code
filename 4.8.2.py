
num_rows = int(input())
num_cols = int(input())

# Note 1: You will need to declare more variables
# Note 2: Place end=' ' at the end of your print statement to separate seats by spaces

for n in range(1, num_rows + 1):
    for l in range(num_cols):
        seat_let = chr(l + 65)
        print('{}{}'.format(n, seat_let), end=' ')
print()


# num_rows = int(input())
# num_cols = int(input())
#
# for n in range(1, num_rows + 1):  # Start seat number from 1
#     for l in range(num_cols):
#         seat_let = chr(l + 65)  # Convert the index to corresponding letter
#         print('{}{}'.format(n, seat_let), end=' ')  # Print seat number and letter
# print()  # Move to the next line after printing all seats
