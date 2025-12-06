# for string x make a dict
# check how many time letter is in string

x = "myszydokazujakiedykotanieczuja"

D = {}

for letter in x:
    if letter not in D.keys():
        D[letter] = 1
    else:
        D[letter] += 1

print(D)
