import  utils


data= [
        {
        'Country':"Mexico",
        'Population' : 120
        },
        {
        'Country':"Col",
        'Population' : 30
        },{
        'Country':"Bol",
        'Population' : 60
        },{
        'Country':"Ar",
        'Population' : 150
        }
    ]

def run():
    keys,values= utils.get_population()

    print(keys,values)


    country = input("Country =>")


    print(utils.population_by_country(data,country))

if __name__ == '__main__':
    run()