class Product:
    def __init__(self, name, store, price):
        self.__name = name
        self.__store = store
        self.__price = price

    def get_name(self):
        return self.__name

    def get_store(self):
        return self.__store

    def get_price(self):
        return self.__price

    def __add__(self, prod_sum):
        if isinstance(prod_sum, Product):
            return self.__price + prod_sum.get_price()

    def __str__(self):
        return f"Товар {self.__name}. Магазин {self.__store}. Цена {self.__price}"


class Storage:
    def __init__(self):
        self.all_products = [
            Product("Планшет", "Apple", 800),
            Product("Телефон", "MTS", 300),
            Product("ПК", "21 vek", 1200),
            Product("Утюг", "5 element", 120),
            Product("Тостер", "Home shop", 60),
            # {"name": "Планшет", "store": "Apple", "price": 800},
            # {"name": "Телефон", "store": "MTS", "price": 300},
            # {"name": "ПК", "store": "21 vek", "price": 1200},
            # {"name": "Утюг", "store": "5 element", "price": 120},
            # {"name": "Тостер", "store": "Home shop", "price": 60},
        ]

    def all(self):
        return self.all_products

    def product_index(self, index):
        if 0 <= index < len(self.all_products):
            product = self.all_products[index]
            return (f"По индексу {index} находится товар: {product.get_name()}, Магазин: {product.get_store()}, "
                    f"Цена: {product.get_price()} руб.")
        else:
            return "Товара на складе нет"

    def product_name(self, name):
        for product in self.all_products:
            if product.get_name().lower() == name.lower():
                return f"Товар {name} находится на складе"
        return f"Товара {name} на складе нет"

    def product_sort_by_name(self):
        self.all_products.sort(key=lambda x: x.get_name())
        return [product.get_name() for product in self.all_products]

    def product_sort_by_store(self):
        self.all_products.sort(key=lambda x: x.get_store())
        return [product.get_store() for product in self.all_products]

    def product_sort_by_price(self):
        self.all_products.sort(key=lambda x: x.get_price())
        return [product.get_price() for product in self.all_products]

    def sum_select_products(self, products):
        return sum(product.get_price() for product in products)


sklad = Storage()
print(sklad.product_index(3))
print(sklad.product_name("Телефон"))
print(sklad.product_sort_by_name())
print(sklad.product_sort_by_store())
print(sklad.product_sort_by_price())

select_prod = [sklad.all_products[0], sklad.all_products[2]]
sum_prod = sklad.sum_select_products(select_prod)
print(f"Цена выбранных: {sum_prod}")
