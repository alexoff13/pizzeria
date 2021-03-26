from pizzeria import Pizza, Order

default_pizzas = [
    ('Пицца1', 'неоч'),
    ('Пицца2', 'получше'),
    ('Пицца3', 'чикибамбони')
]


def check_number(error_message: str) -> int:
    while True:
        try:
            count = int(input())
            break
        except ValueError:
            print(error_message)
    return count


def add_pizza() -> Pizza:
    print('Выберите  номер пиццы, которую хотите добавить в заказ: ')
    print(*(f'{i + 1}. {pizza[0]} {pizza[1]}' for i, pizza in enumerate(default_pizzas)), sep='\n')
    while True:
        try:
            pizza = default_pizzas[check_number('Нужно вводить число, попробуйте еще раз: ') - 1]
            break
        except IndexError:
            print(f'Нужно вводить число от 1 до {len(default_pizzas)}, попробуйте еще раз: ')
    print('Введите размер: ')
    while True:
        try:
            size = int(input())
            new_pizza = Pizza(pizza[0], pizza[1], size)
            break
        except ValueError:
            print('Допустимые размеры: 25, 30, 35, 40. Попробуйте еще раз: ')
    print('Если хотите добавить соль, напишите количество, иначе напишите -1')
    count = check_number('Нужно ввести число, попробуйте еще раз: ')
    if count > 0:
        new_pizza.add_salt(count)
    print('Если хотите добавить сыр, напишите количество, иначе напишите -1')
    count = check_number('Нужно ввести число, попробуйте еще раз: ')
    if count > 0:
        new_pizza.add_cheese(count)

    return new_pizza


if __name__ == '__main__':
    order = Order()
    while True:
        print('Чтобы добавить пиццу нажмите 1, чтобы распечатать нажмите 2, для выхода любую другую кнопку')
        key = input()
        if key == '1':
            order.add_pizza(add_pizza())
        elif key == '2':
            print(order)
        else:
            break
    print('До свидания')
