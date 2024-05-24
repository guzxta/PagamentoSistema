from abc import ABC, abstractmethod

# Interface para os produtos (tipos de pagamento)
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass