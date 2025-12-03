import sys

with open(sys.argv[1], "r") as f:
    banks = [line.strip() for line in f.readlines()]

res = 0
for bank in banks:
    first_battery_idx = 0
    for i in range(1, len(bank) - 11):
        if bank[i] > bank[first_battery_idx]:
            first_battery_idx = i

    second_battery_idx = first_battery_idx + 1
    for i in range(first_battery_idx + 1, len(bank) - 10):
        if bank[i] > bank[second_battery_idx]:
            second_battery_idx = i

    third_battery_idx = second_battery_idx + 1
    for i in range(second_battery_idx + 1, len(bank) - 9):
        if bank[i] > bank[third_battery_idx]:
            third_battery_idx = i

    fourth_battery_idx = third_battery_idx + 1
    for i in range(third_battery_idx + 1, len(bank) - 8):
        if bank[i] > bank[fourth_battery_idx]:
            fourth_battery_idx = i

    fifth_battery_idx = fourth_battery_idx + 1
    for i in range(fourth_battery_idx + 1, len(bank) - 7):
        if bank[i] > bank[fifth_battery_idx]:
            fifth_battery_idx = i

    sixth_battery_idx = fifth_battery_idx + 1
    for i in range(fifth_battery_idx + 1, len(bank) - 6):
        if bank[i] > bank[sixth_battery_idx]:
            sixth_battery_idx = i

    seventh_battery_idx = sixth_battery_idx + 1
    for i in range(sixth_battery_idx + 1, len(bank) - 5):
        if bank[i] > bank[seventh_battery_idx]:
            seventh_battery_idx = i

    eighth_battery_idx = seventh_battery_idx + 1
    for i in range(seventh_battery_idx + 1, len(bank) - 4):
        if bank[i] > bank[eighth_battery_idx]:
            eighth_battery_idx = i

    ninth_battery_idx = eighth_battery_idx + 1
    for i in range(eighth_battery_idx + 1, len(bank) - 3):
        if bank[i] > bank[ninth_battery_idx]:
            ninth_battery_idx = i

    tenth_battery_idx = ninth_battery_idx + 1
    for i in range(ninth_battery_idx + 1, len(bank) - 2):
        if bank[i] > bank[tenth_battery_idx]:
            tenth_battery_idx = i

    eleventh_battery_idx = tenth_battery_idx + 1
    for i in range(tenth_battery_idx + 1, len(bank) - 1):
        if bank[i] > bank[eleventh_battery_idx]:
            eleventh_battery_idx = i

    twelfth_battery_idx = eleventh_battery_idx + 1
    for i in range(eleventh_battery_idx + 1, len(bank)):
        if bank[i] > bank[twelfth_battery_idx]:
            twelfth_battery_idx = i

    highest_joltage = (bank[first_battery_idx] + bank[second_battery_idx] +
        bank[third_battery_idx] + bank[fourth_battery_idx] + bank[fifth_battery_idx] + 
        bank[sixth_battery_idx] + bank[seventh_battery_idx] + bank[eighth_battery_idx] + 
        bank[ninth_battery_idx] + bank[tenth_battery_idx] + bank[eleventh_battery_idx] + 
        bank[twelfth_battery_idx])


    res += int(highest_joltage)

print(res)
