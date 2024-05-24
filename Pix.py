from PaymentFactory import PaymentFactory
from PaymentMethod import PaymentMethod


class Pix(PaymentMethod):
    def pay(self, amount):
        print(f"Pagamento de R${amount} realizado via Pix.")

class PixFactory(PaymentFactory):
    def create_payment_method(self):
        return Pix()