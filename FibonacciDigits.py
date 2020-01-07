# How many fibonnacit digits to print
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

'''
EXAMPLE: fib(10)
'''


'''
# The below code is for python3.7 As you will see in the above code, Python3.8 made some awesome changes that allow this code to be shorteded
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
'''
