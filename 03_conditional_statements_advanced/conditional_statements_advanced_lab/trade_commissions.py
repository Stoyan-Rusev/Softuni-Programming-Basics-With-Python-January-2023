city = input()
volume = float(input())

commission = 0

if volume < 0:
    print("error")

elif city == "Sofia":
    if 0 <= volume <= 500:
        commission = volume * 0.05
    elif 500 < volume <= 1000:
        commission = volume * 0.07
    elif 1000 < volume <= 10000:
        commission = volume * 0.08
    elif volume > 10000:
        commission = volume * 0.12
    print(f'{commission:.2f}')

elif city == "Varna":
    if 0 <= volume <= 500:
        commission = volume * 0.045
    elif 500 < volume <= 1000:
        commission = volume * 0.075
    elif 1000 < volume <= 10000:
        commission = volume * 0.10
    elif volume > 10000:
        commission = volume * 0.13
    print(f'{commission:.2f}')

elif city == "Plovdiv":
    if 0 <= volume <= 500:
        commission = volume * 0.055
    elif 500 < volume <= 1000:
        commission = volume * 0.08
    elif 1000 < volume <= 10000:
        commission = volume * 0.12
    elif volume > 10000:
        commission = volume * 0.145
    print(f'{commission:.2f}')

else:
    print("error")



