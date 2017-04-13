string = str(2**1000)
powersum = 0
for digit in string:
    digit = int(digit)
    powersum += digit
print(powersum)
