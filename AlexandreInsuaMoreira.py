#  Calcula o enesimo número da serie Fibonacci

def recursive_fibonacci(num):
    if num <= 0:
        return 0
    elif num == 1:
        return 1
    else:
        return recursive_fibonacci(num - 1) + recursive_fibonacci(num - 2)


for i in range(0,10):
    print(recursive_fibonacci(i))