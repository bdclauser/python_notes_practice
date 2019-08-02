import random

for i in range(5):
    print(random.random())

print 'Line 6', 2 + 2
print 'Line 7', 2 + 3
print 'Line 8', 4 - 5

print 'Line 10', 5/2

print 'Line 12', 5.0/2

# speed_of_light = 299792458   meters per second
# centimeters = 100            one meter is 100 centimeters
# nanosecond = 1.0/1000000000  one billionth of a second

# Variables
speed_of_light = 299792458.0        # meters per second
centimeters = 100                   # one meter is 100 centimeters
nanosecond = 1.0/1000000000         # one billionth of a second
cycles_per_second = 2700000000.0    # 2.7 GHz

print 'Line 22', speed_of_light * centimeters * nanosecond

print 'Line 24', 299792458 * 100 * 1.0/1000000000 * 1/2.7

# control + r


# print out distance in meters, that light travels in a processor cycle.

cycles_distance = speed_of_light / cycles_per_second

cycles_per_second = 2800000000. # 2.8 GHz
print cycles_distance

print 'Line 35', 'Cycle Distance = ', speed_of_light / cycles_per_second

cycles_distance = speed_of_light / cycles_per_second
print cycles_distance

# What is the value of hours after running this code:
hours = 9
hours = hours + 1
hours = hours * 2

print hours
