items = [
    {
        'product': 'camisa',
        'price':100,
    },{
        'product': 'pantalones',
        'price':200
    },{
        'product': 'pantalones2',
        'price':200
    }
]

prices = list(map(lambda item: item['price'], items))

print(prices)

def add_taxes(item):
    item['taxes'] = item['price'] * .19
    return item

taxes = list(map(add_taxes,items))

print(taxes)