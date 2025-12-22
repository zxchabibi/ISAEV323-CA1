from abc import ABC, abstractmethod
class PaymentSystem(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
    @abstractmethod
    def refund(self, amount):
        pass
class CreditcardPayment(PaymentSystem):
    def pay(self, amount):
        print(f"Оплата картой: {amount} руб")
    def refund(self, amount):
        print(f"Возврат на карту: {amount} руб")
class PayPalPayment(PaymentSystem):
    def pay(self, amount):
        print(f"Оплата через PayPal: {amount} руб")
    def refund(self, amount):
        print(f"Возврат через PayPal: {amount} руб")
card = CreditcardPayment()
card.pay(1000)  
card.refund(500)  
paypal = PayPalPayment()
paypal.pay(2000)  