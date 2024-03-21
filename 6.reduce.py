import functools


numbers = [1,2,3,4]


def acc(counter, item):
    print(f"counter=>{counter}", f"item=>{item}")
    return counter+item

result = functools.reduce(lambda counter, item: counter+item, numbers)

result2 = functools.reduce(acc, numbers)

print(result)