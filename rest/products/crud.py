from dataclasses import dataclass, field


@dataclass
class Product:
    id: int
    name: str
    price: int


# Here are the methods for the project
@dataclass
class ProductsStorage:
    products: dict[int, Product] = field(default_factory=dict)
    last_id: int = 0

    @property
    def next_id(self) -> int:
        self.last_id += 1
        return self.last_id

    @property
    def names(self) -> set[str]:
        return {product.name for product in self.products.values()}

    def add(self, product_name: str, product_price: int) -> Product:
        product = Product(
            id=self.next_id,
            name=product_name,
            price=product_price,
        )
        self.products[product.id] = product
        return product

    def get_list(self) -> list[Product]:
        return list(self.products.values())

    def get_by_id(self, product_id: int) -> Product | None:
        return self.products.get(product_id)

    def name_exists(self, product_name: str) -> bool:
        # Here we check if the name already exists
        return product_name in self.names

    def delete(self, product_id: int) -> None:
        self.products.pop(product_id, None)


products_storage = ProductsStorage()


products_storage.add(
    "Motherboard",
    200,
)

products_storage.add(
    "CPU",
    300,
)

products_storage.add(
    "GPU",
    400,
)

products_storage.add(
    "RAM",
    100,
)

products_storage.add(
    "SSD",
    100,
)

products_storage.add(
    "Power Supply",
    100,
)

products_storage.add(
    "Case",
    100,
)
