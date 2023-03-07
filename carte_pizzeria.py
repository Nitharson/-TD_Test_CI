class CartePizzeria:
    def __init__(self):
        self.pizzas = []

    def is_empty(self):
        return len(self.pizzas) == 0

    def nb_pizzas(self):
        return len(self.pizzas)

    def add_pizza(self, pizza):
        self.pizzas.append(pizza)

    def remove_pizza(self, name):
        for i in range(len(self.pizzas)):
            if self.pizzas[i].name == name:
                del self.pizzas[i]
                return
