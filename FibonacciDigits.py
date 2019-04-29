# How many fibonnacit digits to print

a = int(input('How many Fibonacci digits do you want to see?: '))

if a == 1:
    b = [1]

elif a != 1:
    b = [1,1]

    for i in b:
        if len(b) < a:
            i = b[-1] + b[-2]
            b.append(i)

print(b)
