import random

print(random.randint(5, 20))  # line 1
# I saw 6 on line 1.
# The smallest possible I could have seen was 5 and the largest was 20.

print(random.randrange(3, 10, 2))  # line 2
# I saw 5 on line 2.
# The smallest possible I could have seen was 3 and the largest was 9.
# No, because it starts at 3 with an increment of 2. So, the possible results are 3, 5, 7 and 9.

print(random.uniform(2.5, 5.5))  # line 3
# I saw 4.363298232820304 on line 3.
# The smallest possible I could have seen was 2.5 and the largest was 5.5.

# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
print(random.randint(1, 100))
