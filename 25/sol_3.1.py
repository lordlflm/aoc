import sys

with open(sys.argv[1], "r") as f:
    banks = [line.strip() for line in f.readlines()]

res = 0
for bank in banks:
    first_battery_idx = 0
    for i in range(1, len(bank) - 1):
        if bank[i] > bank[first_battery_idx]:
            first_battery_idx = i

    second_battery_idx = first_battery_idx + 1
    for i in range(first_battery_idx + 1, len(bank)):
        if bank[i] > bank[second_battery_idx]:
            second_battery_idx = i

    highest_joltage = bank[first_battery_idx] + bank[second_battery_idx]
    res += int(highest_joltage)

print(res)
