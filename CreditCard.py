from PaymentFactory import PaymentFactory
from PaymentMethod import PaymentMethod


class CreditCard(PaymentMethod):
    def pay(self, amount):
        print(f"Pagamento de R${amount} realizado com cartão de crédito.")

class CreditCardFactory(PaymentFactory):
    def create_payment_method(self):
        return CreditCard()