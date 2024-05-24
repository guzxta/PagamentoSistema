# Cliente
from CreditCard import CreditCardFactory
from DebitCard import DebitCardFactory
from Pix import PixFactory


class PaymentProcessor:
    def __init__(self, factory):
        self.factory = factory

    def purchase(self, amount):
        payment_method = self.factory.create_payment_method()
        payment_method.pay(amount)

# Uso
if __name__ == "__main__":
    # Escolha o tipo de pagamento
    payment_type = input("Escolha o tipo de pagamento (1: Pix /2: Cartão de Crédito /3:Cartão de Débito): ").lower()

    # Crie a fábrica com base na escolha
    if payment_type == "1":
        factory = PixFactory()
    elif payment_type == "2":
        factory = CreditCardFactory()
    elif payment_type == "3":
        factory = DebitCardFactory()
    else:
        print("Tipo de pagamento inválido.")
        exit()

    # Processe o pagamento
    payment_processor = PaymentProcessor(factory)
    amount = float(input("Digite o valor a ser pago: "))
    payment_processor.purchase(amount)