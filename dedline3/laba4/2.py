class CreditCard:
    def __init__(self, a, b, c, d=0): 
        self.__number = a  
        self.__cvc = b  
        self.owner_name = c  
        self._balance = d 
    def __check_pin(self, p):  
        return p == "1234"
    def pay(self, i, f): 
        if i > 0 and i <= self._balance and self.__check_pin(f):
            self._balance -= i
            return True
        return False
    def get_balance(self):  
        return self._balance
card = CreditCard("1234567890123456", "123", "Иван", 1000)
print(f"Владелец: {card.owner_name}")  
print(f"Баланс: {card.get_balance()}")  
if card.pay(500, "1234"):
    print("Оплата прошла")
    print(f"Новый баланс: {card.get_balance()}")
else:
    print("Ошибка")