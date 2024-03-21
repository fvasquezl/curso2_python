"""Lists"""

numbers = []
for element in range(1,11):
    numbers.append(element*2)

print(numbers)

"""List Comprehension"""

numbers2= [i*2 for i in range(1,11)]
print(numbers2)


numbers2= [i*2 for i in range(1,11) if i%2==0 ]
print(numbers2)