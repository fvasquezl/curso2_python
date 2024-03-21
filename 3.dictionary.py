import random


dict= {}
for i in range(1,11):
    dict[i]=i*2

print(dict)

""" dict comprehension"""

dict2 = {x:x*2  for x in range(1,10)}
print(dict2)

countries =['col','mex','bol','pe']
population = {}

for country in countries:
    population[country]= random.randint(1, 100)
print(population)

population = {country:random.randint(1,100) for country in countries}
print(population)

""" ZIP  and ditcionary """

names = ['faus','seb','bib']
ages = [52,15,50]
dict3 = {name:age for (name, age) in zip(names,ages)} 
print(dict3)

""" Condition dictionary """



population_v2 = {country:random.randint(1,100) for country in countries}
print(population)

result = {country:population for (country,population) in population_v2.items() if population>20}
print(result)


text = "Hola, soy Nicolas"
unique = {c:c.upper() for c in text if c in 'aeiou'}

print(unique)

text = "Hola, soy Nicolas"
unique = {c:text.count(c) for c in text if c in 'aeiou'}

print(unique)



