from dataclasses import dataclass, field
@dataclass(frozen=True)  
class продукты:
    name: str
    price: float = field(repr=False)  
    weight: float
    is_available: bool = True
    def order_cost(self, quantity):
        return self.price * quantity
apple = продукты("яблоко", 15.0, 0.2, True)
print(apple)  
print(apple.order_cost(10))  