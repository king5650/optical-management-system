"""
api_client.py — Central HTTP layer

WHY THIS EXISTS
───────────────
Every API call in the app goes through this class. Benefits:
  • One place to change the base URL (dev → production).
  • Auth token/cookie handled once — not repeated in every panel.
  • Consistent error format returned to all callers.
  • Easy to mock in tests.

CONNECTION FLOW (every request):
  Panel calls ApiClient method
    → requests.Session sends HTTP request with session cookie
    → Django view processes it
    → JSON response parsed and returned as Python dict
    → Panel updates UI from that dict
"""

import requests

BASE_URL = "http://127.0.0.1:8000/auth"   # change to your server address


# class ApiError(Exception):
#     """Raised when the server returns a non-2xx response."""
#     def __init__(self, message: str, status_code: int = 0):
#         super().__init__(message)
#         self.status_code = status_code


# class ApiClient:
#     """
#     Wraps requests.Session so the Django session cookie is sent on every
#     request automatically after login — no manual token management needed.
#     """

#     def __init__(self):
#         self.session = requests.Session()
#         self.session.headers.update({"Content-Type": "application/json"})

#     # ──────────────────────────────────────────────────────────────────────
#     # Internal helpers
#     # ──────────────────────────────────────────────────────────────────────

#     def _url(self, path: str) -> str:
#         return f"{BASE_URL}/{path.lstrip('/')}"

#     def _handle(self, response: requests.Response) -> dict:
#         """
#         Parse response and raise ApiError on failure.
#         All callers get a plain dict on success — no response object leaks out.
#         """
#         try:
#             data = response.json()
#         except Exception:
#             data = {"error": response.text or "Empty response"}

#         if not response.ok:
#             msg = data.get("error") or data.get("detail") or f"HTTP {response.status_code}"
#             raise ApiError(msg, response.status_code)

#         return data

#     def get(self, path: str, params: dict = None) -> dict:
#         r = self.session.get(self._url(path), params=params)
#         return self._handle(r)

#     def post(self, path: str, body: dict = None) -> dict:
#         r = self.session.post(self._url(path), json=body or {})
#         return self._handle(r)

#     def patch(self, path: str, body: dict = None) -> dict:
#         r = self.session.patch(self._url(path), json=body or {})
#         return self._handle(r)

#     def delete(self, path: str) -> dict:
#         r = self.session.delete(self._url(path))
#         return self._handle(r)

#     # ──────────────────────────────────────────────────────────────────────
#     # Auth
#     # ──────────────────────────────────────────────────────────────────────

#     def login(self, username: str, password: str) -> dict:
#         return self.post("login/", {"username": username, "password": password})

#     # ──────────────────────────────────────────────────────────────────────
#     # Dashboard
#     # ──────────────────────────────────────────────────────────────────────

#     def dashboard_counts(self) -> dict:
#         return self.get("dashboard-counts/")

#     # ──────────────────────────────────────────────────────────────────────
#     # Patients
#     # ──────────────────────────────────────────────────────────────────────

#     def list_patients(self) -> dict:
#         return self.get("patients/list/")

#     def search_patients(self, query: str) -> dict:
#         return self.get("patients/search/", params={"q": query})

#     def add_patient(self, data: dict) -> dict:
#         return self.post("patients/add/", data)

#     def update_patient(self, patient_id: int, data: dict) -> dict:
#         return self.post(f"patients/update/{patient_id}/", data)

#     def delete_patient(self, patient_id: int) -> dict:
#         return self.delete(f"patients/delete/{patient_id}/")

#     # ──────────────────────────────────────────────────────────────────────
#     # Orders
#     # ──────────────────────────────────────────────────────────────────────

#     def list_orders(self, status: str = None) -> dict:
#         params = {"status": status} if status else None
#         return self.get("orders/", params=params)

#     def create_order(self, data: dict) -> dict:
#         return self.post("orders/", data)

#     def get_order(self, order_id: int) -> dict:
#         return self.get(f"orders/{order_id}/")

#     def update_order(self, order_id: int, data: dict) -> dict:
#         return self.patch(f"orders/{order_id}/", data)

#     def order_summary(self, order_id: int) -> dict:
#         return self.get(f"orders/{order_id}/summary/")

#     def change_order_status(self, order_id: int, new_status: str) -> dict:
#         return self.post(f"orders/{order_id}/change-status/", {"status": new_status})

#     def cancel_order(self, order_id: int) -> dict:
#         return self.post(f"orders/{order_id}/cancel/")

#     def order_history(self, order_id: int) -> dict:
#         return self.get(f"orders/{order_id}/history/")

#     # ──────────────────────────────────────────────────────────────────────
#     # Payments
#     # ──────────────────────────────────────────────────────────────────────

#     def add_payment(self, order_id: int, amount: float,
#                     method: str, reference: str = "") -> dict:
#         return self.post("payments/", {
#             "order": order_id,
#             "amount": str(amount),
#             "payment_method": method,
#             "transaction_reference": reference,
#         })

#     def payments_by_order(self, order_id: int) -> dict:
#         return self.get(f"payments/by-order/{order_id}/")

#     def refund_payment(self, order_id: int, amount: float) -> dict:
#         return self.post(f"payments/refund/{order_id}/", {"amount": str(amount)})

#     # ──────────────────────────────────────────────────────────────────────
#     # Inventory (existing endpoints)
#     # ──────────────────────────────────────────────────────────────────────

#     def fetch_inventory(self) -> dict:
#         return self.get("inventory/items/")

#     def list_frames(self) -> dict:
#         return self.get("inventory/frames/list/")

#     def list_lenses(self) -> dict:
#         return self.get("inventory/lenses/list/")


# # Shared singleton — import this in every panel
# api = ApiClient()
"""
api_client.py — updated version

CHANGES FROM PREVIOUS VERSION
──────────────────────────────
Four new methods added to support the cascaded Create Order form:

  prescriptions_by_patient(patient_id)
    → GET /api/prescriptions/by-patient/<id>/
    → Called when patient is selected in the form.
    → Returns that patient's MedicalReports for the prescription dropdown.

  categories()
    → GET /api/categories/
    → Returns all ItemCategory rows for the first product dropdown.
    → Already existed on backend — method was just missing on frontend.

  item_types_by_category(category_id)
    → GET /api/item-types/by-category/<id>/
    → Called when a category is selected.
    → Returns ItemTypes in that category for the second product dropdown.

  inventory_items_by_type(type_id)
    → GET /api/inventory/by-type/<id>/
    → Called when an item type is selected.
    → Returns InventoryItems of that type for the third dropdown.
    → Includes unit_price so the price field can be auto-filled.

HOW THE SESSION COOKIE WORKS:
  After api.login() succeeds, Django sets a session cookie in
  self.session (a requests.Session object). Every subsequent call
  through self.session automatically includes that cookie, so the
  user stays authenticated without any manual header management.

  If a request returns 403 (not authenticated), the frontend should
  redirect to the login window.
"""

import requests

BASE_URL = "http://127.0.0.1:8000/auth"   # ← change this for production


class ApiError(Exception):
    """Raised when the server returns a non-2xx status code."""
    def __init__(self, message: str, status_code: int = 0):
        super().__init__(message)
        self.status_code = status_code


class ApiClient:
    """
    Thin HTTP wrapper around requests.Session.
    One instance is shared across the whole app (see singleton `api` at bottom).
    """

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json"})

    # ──────────────────────────────────────────────────────────────────────
    # Internal helpers
    # ──────────────────────────────────────────────────────────────────────

    def _url(self, path: str) -> str:
        return f"{BASE_URL}/{path.lstrip('/')}"

    def _handle(self, response: requests.Response) -> dict:
        """
        Parse JSON, raise ApiError on non-2xx.
        All callers receive a plain dict — no raw Response objects leak out.
        """
        try:
            data = response.json()
        except Exception:
            data = {"error": response.text or "Empty response"}

        if not response.ok:
            # Prefer detailed server-side validation messages when present
            if isinstance(data, dict):
                # DRF validation errors typically appear under 'errors' or as a dict
                if "errors" in data:
                    msg = data["errors"]
                elif "error" in data:
                    msg = data["error"]
                elif "detail" in data:
                    msg = data["detail"]
                else:
                    msg = data
            else:
                msg = data

            # Ensure message is a string for the exception
            try:
                msg_str = str(msg)
            except Exception:
                msg_str = f"HTTP {response.status_code}"

            raise ApiError(msg_str, response.status_code)

        return data

    def get(self, path: str, params: dict = None) -> dict:
        r = self.session.get(self._url(path), params=params)
        return self._handle(r)

    def has_session(self) -> bool:
      """Return True if the requests.Session contains a Django session cookie.

      This is a lightweight way for the UI to know whether the user has
      previously authenticated (login stored a session cookie). It is
      not foolproof but prevents unauthenticated POSTs that would
      redirect to /accounts/login/.
      """
      # Common Django session cookie name is 'sessionid'. Fall back to
      # checking any cookie that contains 'session' in its name.
      for name in self.session.cookies.keys():
        if "session" in name.lower():
          return True
      return False

    def post(self, path: str, body: dict = None) -> dict:
        r = self.session.post(self._url(path), json=body or {})
        return self._handle(r)

    def patch(self, path: str, body: dict = None) -> dict:
        r = self.session.patch(self._url(path), json=body or {})
        return self._handle(r)

    def delete(self, path: str) -> dict:
        r = self.session.delete(self._url(path))
        return self._handle(r)

    # ──────────────────────────────────────────────────────────────────────
    # Auth
    # ──────────────────────────────────────────────────────────────────────

    def login(self, username: str, password: str) -> dict:
        return self.post("login/", {"username": username, "password": password})

    # ──────────────────────────────────────────────────────────────────────
    # Dashboard
    # ──────────────────────────────────────────────────────────────────────

    def dashboard_counts(self) -> dict:
        return self.get("dashboard-counts/")

    # ──────────────────────────────────────────────────────────────────────
    # Patients
    # ──────────────────────────────────────────────────────────────────────

    def list_patients(self) -> dict:
        return self.get("patients/list/")

    def search_patients(self, query: str) -> dict:
        return self.get("patients/search/", params={"q": query})

    def add_patient(self, data: dict) -> dict:
        return self.post("patients/add/", data)

    def update_patient(self, patient_id: int, data: dict) -> dict:
        return self.post(f"patients/update/{patient_id}/", data)

    def delete_patient(self, patient_id: int) -> dict:
        return self.delete(f"patients/delete/{patient_id}/")

    # ──────────────────────────────────────────────────────────────────────
    # Prescriptions  (NEW)
    # ──────────────────────────────────────────────────────────────────────

    def prescriptions_by_patient(self, patient_id: int) -> dict:
        """
        GET /api/prescriptions/by-patient/<patient_id>/

        Called immediately when the user selects a patient in the
        Create Order form. Returns that patient's MedicalReports so
        the prescription dropdown can be populated.

        RESPONSE:
          {
            "reports": [
              {"id": 7, "reference_id": "REF-2025-007", "date": "2025-11-03"},
              {"id": 3, "reference_id": "REF-2025-003", "date": "2025-08-15"}
            ]
          }
        """
        return self.get(f"medical-reports/list/{patient_id}/")

    # ──────────────────────────────────────────────────────────────────────
    # Inventory — cascaded dropdown data  (NEW / UPDATED)
    # ──────────────────────────────────────────────────────────────────────

    def categories(self) -> dict:
        """
        GET /api/categories/

        Returns all ItemCategory rows.
        Used to populate the first dropdown in Create Order form.

        RESPONSE:
          {"categories": [{"id": 1, "name": "Frames"}, ...]}

        NOTE: The existing backend endpoint returns a key that may differ
        (check your fetch_categories view). If the key is not "categories",
        update the frontend code that reads from this response.
        """
        return self.get("categories/")

    def item_types_by_category(self, category_id: int) -> dict:
        """
        GET /api/item-types/by-category/<category_id>/

        Called when the user selects a category (e.g. "Lenses").
        Returns all ItemType rows in that category.

        RESPONSE:
          {
            "item_types": [
              {"id": 3, "name": "VIP"},
              {"id": 4, "name": "Simple Vision"}
            ]
          }
        """
        return self.get(f"item-types/by-category/{category_id}/")

    def inventory_items_by_type(self, type_id: int) -> dict:
        """
        GET /api/inventory/by-type/<type_id>/

        Called when the user selects an item type (e.g. "VIP").
        Returns InventoryItem rows of that type — usually just one,
        but could be multiple at different price points.

        RESPONSE:
          {
            "items": [
              {
                "id": 12,
                "type_name": "VIP",
                "category_name": "Lenses",
                "unit_price": "45000.00",
                "stock_level": 8,
                "is_low_stock": false
              }
            ]
          }

        WHAT THE FORM DOES WITH THIS:
          - Populates the product dropdown.
          - When one is selected: auto-fills price field with unit_price.
          - Shows "(8 in stock)" next to the item name.
          - Shows a ⚠ warning if is_low_stock is true.
        """
        return self.get(f"inventory/by-type/{type_id}/")

    def fetch_inventory(self) -> dict:
        """GET /api/inventory/items/ — full inventory list (existing)."""
        return self.get("inventory/items/")

    # ──────────────────────────────────────────────────────────────────────
    # Orders
    # ──────────────────────────────────────────────────────────────────────

    def list_orders(self, status: str = None) -> dict:
        params = {"status": status} if status else None
        return self.get("orders/", params=params)

    def create_order(self, data: dict) -> dict:
        """
        POST /api/orders/

        CHANGE FROM PREVIOUS VERSION:
          No longer sends 'order_number' in the payload.
          The backend generates it automatically inside OrderService.
          The response includes the generated order_number.

        PAYLOAD:
          {
            "patient":      3,
            "prescription": 7,
            "discount":     "0.00",
            "notes":        "...",
            "items": [
              {
                "product":    12,       ← InventoryItem.id
                "quantity":   1,
                "unit_price": "45000",
                "item_type":  "Lenses"  ← ItemCategory.name (label only)
              }
            ]
          }
        """
        return self.post("orders/", data)

    def get_order(self, order_id: int) -> dict:
        return self.get(f"orders/{order_id}/")

    def update_order(self, order_id: int, data: dict) -> dict:
        return self.patch(f"orders/{order_id}/", data)

    def order_summary(self, order_id: int) -> dict:
        return self.get(f"orders/{order_id}/summary/")

    def change_order_status(self, order_id: int, new_status: str) -> dict:
        return self.post(
            f"orders/{order_id}/change-status/",
            {"status": new_status}
        )

    def cancel_order(self, order_id: int) -> dict:
        return self.post(f"orders/{order_id}/cancel/")

    def order_history(self, order_id: int) -> dict:
        return self.get(f"orders/{order_id}/history/")

    # ──────────────────────────────────────────────────────────────────────
    # Payments
    # ──────────────────────────────────────────────────────────────────────

    def add_payment(self, order_id: int, amount: float,
                    method: str, reference: str = "") -> dict:
        return self.post("payments/", {
            "order":                order_id,
            "amount":               str(amount),
            "payment_method":       method,
            "transaction_reference": reference,
        })

    def payments_by_order(self, order_id: int) -> dict:
        return self.get(f"payments/by-order/{order_id}/")

    def refund_payment(self, order_id: int, amount: float) -> dict:
        return self.post(
            f"payments/refund/{order_id}/",
            {"amount": str(amount)}
        )


# ── Shared singleton ──────────────────────────────────────────────────────────
# Import this in every panel:  from api_client import api
api = ApiClient()