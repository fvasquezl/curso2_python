numbers = [1,2,3,4,5,6,7]

result1 =[]
for i in numbers:
    result1.append(i+2)

print(result1)

"""
funcion map
"""

result2 = list(map(lambda x: x+2, numbers))

print(result2)

numbers_1=[1,2,3,4]
numbers_2=[5,6,7]

result3 = list(map(lambda x,y: x+y, numbers_1,numbers_2))
print(result3)  

"""[6, 8, 10] """