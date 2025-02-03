for i in range(1, 21, 2):
    print(i, end=" ")
print()

# a.
for i in range(0, 101, 10):
    print(i, end=" ")
print()

# b.
for i in range(20, 0, -1):
    print(i, end=" ")
print()

# c.
star_count = int(input("Number of stars: "))
for i in range(star_count):
    print("*", end="")
print()

# d.
star_count = int(input("Number of stars: "))
for i in range(1, star_count + 1):
    print("*" * i)
print()


