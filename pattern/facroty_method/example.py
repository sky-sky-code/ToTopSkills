from abc import ABC, abstractmethod


class Factory(ABC):

    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self):
        product = self.factory_method()
        return product.get_product()


class AppleFactory(Factory):

    def factory_method(self):
        return AppleProduct()


class PineappleFactory(Factory):

    def factory_method(self):
        return PineappleFactory()


class Product(ABC):

    @abstractmethod
    def get_product(self) -> str:
        pass


class AppleProduct(Product):

    def get_product(self) -> str:
        return 'apple'


class Pineapple(Product):

    def get_product(self) -> str:
        return 'pineapple'


def client_code(factory: Factory):
    return factory.some_operation()


def main():
    product = input("Введите продукт")
    if product == 'apple':
        factory = AppleFactory()
    else:
        factory = PineappleFactory()
    return client_code(factory)


print(main()) 
