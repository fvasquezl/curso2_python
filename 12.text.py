file = open('./text.txt')

# print(file.read())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())


for line in file:
    print(line)

file.close()

'''most common way'''

with open('./text.txt') as file:
    for line in file:
        print(line)