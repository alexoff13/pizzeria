class Pizza:
    def __init__(self, name: str, description: str, size: int):
        if size not in [25, 30, 35, 40]:
            raise ValueError('Недопустимый размер')
        self._price = size * 100 + len(description) * 2
        self._size = size
        self._description = description
        self._name = name
        self._salt = 0
        self._cheese = 0

    @property
    def price(self):
        return self._price

    def add_salt(self, count):
        self._price += count * 10
        self._salt += count

    def add_cheese(self, count):
        self._price += count * 20
        self._cheese += count

    def __str__(self):
        return f'Пицца {self._name}. Размер: {self._size}. Описание: {self._description} Цена: {self._price}\n   ' \
               f'Количество соли: {self._salt}. Количество сыра: {self._cheese}'


class Order:
    def __init__(self):
        self._pizzas = []

    def add_pizza(self, pizza: Pizza):
        self._pizzas.append(pizza)

    def remove_pizza(self, pizza: Pizza):
        self._pizzas.remove(pizza)

    def __str__(self):
        return ''.join(f'{i + 1}. {pizza}\n' for i, pizza in enumerate(self._pizzas)) \
               + f'Итоговая сумма заказа: {sum(i.price for i in self._pizzas)}'
