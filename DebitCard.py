from PaymentFactory import PaymentFactory
from PaymentMethod import PaymentMethod


class DebitCard(PaymentMethod):
    def pay(self, amount):
        print(f"Pagamento de R${amount} realizado com cartão de débito.")

class DebitCardFactory(PaymentFactory):
    def create_payment_method(self):
        return DebitCard()