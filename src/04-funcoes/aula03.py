""" Exemplos de funções """

# Função usando *args
def world_cup_titles(country, *args):
    print('Country: ', country)
    for title in args:
        print('year: ', title)

world_cup_titles('Brasil', '1958', '1962', '1970', '1994', '2002')
Country:  'Brasil'
Year:  1958
Year:  1962
Year:  1970
Year:  1994
Year:  2002      

world_cup_titles('Espanha', '2010')
Country:  'Espanha'
Year:  2010

print('----------------')

# Função usando **kwargs
def calculate_price(value, **kwargs):
    tax_percentage = kwargs.get('tax_percentage')
    discount = kwargs.get('discount')
    if tax_percentage:
        value += value * (tax_percentage / 100)
    if discount:
        value -= discount
    return value

final_price = calculate_price(100.0)
print(final_price)

final_price = calculate_price(100.0, discount=5.0)
print(final_price)

final_price = calculate_price(100.0, tax_percentage=7)
print(final_price)

final_price = calculate_price(100.0, tax_percentage=7, discount=5.0)
print(final_price)
