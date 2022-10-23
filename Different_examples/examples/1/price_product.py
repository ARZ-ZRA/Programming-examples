# Напишите функцию, которая будет принимать старую и
# новую цену товара и возвращать процент, на который
# цена повысилась или понизилась.
def prise_product(old_price, new_price):
    price_proc =  (old_price-new_price)/old_price
    if old_price < new_price:
        print('Product rise in price by {:.2%}'.format(abs(price_proc)))
    elif old_price>new_price:
        print(f'Product fell by {abs(price_proc):.2f}')
    else:
        print(f'The price of the product has not changed and coast = {old_price}')

def percentage_changed(old, new):
    old, new = int(old[:-1]), int(new[:-1])
    return '{:.0%} {}'.format(abs(old - new) / old, 'increase' if new > old else 'decrease')
def percentage_changed_1(old, new):
    p = int(new[:-1]) / int(old[:-1])
    return '{:.0%} {}crease'.format(abs(p - 1), ('de', 'in')[p > 1])


print(percentage_changed("800$", "920$"))
prise_product(800,920)