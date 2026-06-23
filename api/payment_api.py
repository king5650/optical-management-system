from .client import ApiClient

class PaymentAPI:

    @staticmethod
    def add_payment(data):
        return ApiClient.post("/payments/", data)