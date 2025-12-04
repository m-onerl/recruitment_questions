# What data structure would you use to store phone numbers
# of all company clients and their corresponding surnames? Choose a structure such that
# checking the owner of a phone number doesn't take much time.

# Then create an example structure storing the following information:
# 123456789 - Jan Kot
# 999888777 - Anna Lis
# 111222333 - Jan Kot
# Read the surname of the owner of number 123456789


phone_numbers = {123456789: 'Jan Kot',
                 999888777: 'Anna Lis', 111222333: 'Jan Kot'}

print(phone_numbers)
print(phone_numbers[123456789])


D = {'imie': 'Anna', 'imie': 'Lena', 'imie': 'Kazimierz'}

print(D)
