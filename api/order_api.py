from .client import ApiClient

class OrderAPI:

    @staticmethod
    def get_orders():
        return ApiClient.get("/orders/")

    @staticmethod
    def create_order(data):
        return ApiClient.post("/orders/", data)

    @staticmethod
    def get_order(order_id):
        return ApiClient.get(f"/orders/{order_id}/")

    @staticmethod
    def change_status(order_id, status):
        return ApiClient.post(f"/orders/{order_id}/change_status/", {"status": status})