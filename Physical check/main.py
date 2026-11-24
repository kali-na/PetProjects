name_shop = input('Введите название магазина: ')

products = []

while True:
    name_product = input('Введите название товара или "СТОП": ')
    if name_product.upper() == 'СТОП':
        break

    price_product = float(input('Введите цену товара: '))
    quantity_products = int(input('Введите количество товара: '))

    products.append({
        'name': name_product,
        'price': price_product,
        'quantity': quantity_products,
    })

total_sum = 0

with open('Check.txt', 'w', encoding='utf-8') as file:
    file.write('=============== ЧЕК ===============\n')
    file.write(f'{"Товар":<15}{"Цена":>10}{"Кол-во":>10}{"Сумма":>12}\n')
    file.write('-' * 47 + '\n')

    for product in products:
        line_sum = product['price'] * product['quantity']
        total_sum += line_sum
        file.write(
            f"{product['name']:<15}{product['price']:>10.2f}"
            f"{product['quantity']:>10}{line_sum:>12.2f}\n"
        )

        file.write('-' * 47 + '\n')
        file.write(f'ИТОГО: {total_sum:.2f} руб.\n')

print('Чек сохранён в файл ЧЕК.txt')
