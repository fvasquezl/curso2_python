import csv
from functools import reduce


def read_csv(path):
   # Tu código aquí 👇
   with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile,delimiter=",")
        total = reduce(lambda x,y:x+y, list(int(x[-1]) for x in reader ))       
   return total

response = read_csv('./data.csv')
print(response)