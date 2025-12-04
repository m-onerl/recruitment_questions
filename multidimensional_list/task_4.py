# Create the cabinet which one have 3 drawers with 3 compartments inside
# make model and add string "pen" into it
# into middle drawers in middle compartments


szafka = [[[], [], []], [[], [], []], [[], [], []]]

# szafka[1][1] = ['pen']
szafka[1][1].append('pen')

for szuflada in szafka:
    print(szuflada)
