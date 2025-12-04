# create code where we can check the most diffrence between tuple and list:

L = [1, 2, 3, True, (1, 2)]
T = (4, 5, 6, False, ['x', 'y'])

L[2] = 'X'
print(L)
# T[3] = 'X'
print(T)
