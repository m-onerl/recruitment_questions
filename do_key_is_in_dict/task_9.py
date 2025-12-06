# for string x make a dict
# check how many time letter is in string

# x = "myszydokazujakiedykotanieczuja"

# D = {}

# for letter in x:
#     if letter not in D.keys():
#         D[letter] = 1
#     else:
#         D[letter] += 1

# print(D)

S = {x: x+1 for x in range(10000) if x % 23 == 0}


def check_numbers():
    for number in S:
        if number in S.keys() == 7340:
            return True
        else:
            return False


print(check_numbers())
