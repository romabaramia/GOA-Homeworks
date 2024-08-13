number = 1

while number <= 100:
    if 50 <= number <= 60:
        number += 1
        continue
    print(number)

sum = 0
i = 1

while sum < 50:
    sum += i
    i += 1

    print (sum)
    print (i-1)