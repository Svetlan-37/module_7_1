class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self, __file_name='products.txt'):
        self.__file_name = __file_name

    def get_products(self):
        file = open(self.__file_name, 'r')
        read = file.read()
        file.close()
        return read

    def add(self, *products):
        for i in products:
            i = (str(i))
            if i in self.get_products():
                print(f'Продукт {i} уже есть в магазине')
            else:
                file = open(self.__file_name, 'a')
                file.write(f'\n{i}')
                file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vagetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vagetables')


print(p2)
s1.add(p1, p2, p3)
print(s1.get_products())
