import random

for i in range(5):
    print(random.random())

print('Line 6', 2 + 2)
print('Line 7', 2 + 3)
print('Line 8', 4 - 5)

print('Line 10', 5 / 2)

print('line 12', 5.0 / 2)

# speedOfLight = 299792458 meters per second
# centimeters = 100 one meter is 100 centimeters
# nanosecond = 1.0/1000000000 one billionth of a second

# Variables
speedOfLight = 299792458.0  # meters per second
centimeters = 100  # one meter is 100 centimeters
nanosecond = 1.0 / 1000000000  # one billionth of a second
cyclesPerSecond = 2700000000.0  # 2.7 GHz

print('Line 24', speedOfLight * centimeters * nanosecond)

print('Line 26', 299792458 * 100 * 1.0 / 1000000000 * 1 / 2.7)

# control + r

# print out distance in meters, tht light travels in a processor cycle.

cyclesPerSecond = 2800000000  # 2.8 GHz
print(cyclesPerSecond)

print('Line 35', 'Cycle Distance = ', speedOfLight / cyclesPerSecond)

cyclesDistance = speedOfLight / cyclesPerSecond
print(cyclesDistance)

# What is the value of hours after running this code:
hours = 9
hours = hours + 1
hours = hours * 2

print(hours)