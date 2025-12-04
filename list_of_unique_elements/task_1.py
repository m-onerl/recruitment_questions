# list_of_unique_elements
# using the list A
# make list B which one have only unique elements from list A


A = [1, 2, 3, 3, 2, 1, 2, 3]  # -> B = [1,2,3]

B = []

for element in A:
    if element not in B:
        B.append(element)
print(B)

B = list(set(A))

print(B)
