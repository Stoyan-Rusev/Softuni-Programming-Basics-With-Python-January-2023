from sys import maxsize

n = int(input())

odd_sum = 0
odd_min = maxsize
odd_max = - maxsize

even_sum = 0
even_min = maxsize
even_max = -maxsize

for i in range(1, n + 1):
    number = float(input())

    if i % 2 == 0:
        even_sum += number
        if number < even_min:
            even_min = number
        if number > even_max:
            even_max = number

    else:
        odd_sum += number
        if number < odd_min:
            odd_min = number
        if number > odd_max:
            odd_max = number

print(f"OddSum={odd_sum:.2f},")

if odd_min != maxsize:
    print(f"OddMin={odd_min:.2f},")
else:
    print("OddMin=No,")

if odd_max != - maxsize:
    print(f"OddMax={odd_max:.2f},")
else:
    print("OddMax=No,")


print(f"EvenSum={even_sum:.2f},")

if even_min != maxsize:
    print(f"EvenMin={even_min:.2f},")
else:
    print("EvenMin=No,")

if even_max != - maxsize:
    print(f"EvenMax={even_max:.2f}")
else:
    print("EvenMax=No")
