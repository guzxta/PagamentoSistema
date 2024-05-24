from abc import ABC, abstractmethod


class PaymentFactory(ABC):
    @abstractmethod
    def create_payment_method(self):
        pass