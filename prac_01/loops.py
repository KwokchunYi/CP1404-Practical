# loops.py

for number in range(1, 21, 2):
    print(number, end=' ')

# Task a.count in 10s from 0 to 100:
print("Task a:")
for i in range(0, 101, 10):
    print(i, end=' ')
print("\n")

# Task b.count down form 20 to 1:
print("Task b:")
for i in range(1, 21, 1):
    print(i, end= '')
print("\n")

# Task c.print n stars:
print("Task c:")
n = int(input("Number of stars: "))
print("*" * n)
print("\n")

# Task d: Print n lines of increasing stars
print("Task d:")
n = int(input("Number of stars for increasing lines: "))
for i in range(1, n + 1):
    print("*" * i)