sumsq = 0
for i in range(1, 101):
    sumsq += i ** 2

sqsum = 0
for i in range(1, 101):
    sqsum += i

print(sumsq)
print(sqsum)
sqsum = sqsum ** 2
print(sqsum)
print()
print(sqsum - sumsq)
