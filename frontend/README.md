# Optical Cabinet — PySide6 Frontend

## Folder structure

```
frontend/
│
├── main.py                         ← Run this to start the app
├── api_client.py                   ← All HTTP calls (one place)
├── requirements.txt
│
├── assets/
│   ├── styles.py                   ← Global colours + stylesheet
│   └── __init__.py
│
├── workers/
│   ├── api_worker.py               ← Background thread for API calls
│   └── __init__.py
│
└── windows/
    ├── login_window.py             ← Login screen
    ├── main_window.py              ← Sidebar + content area
    ├── __init__.py
    │
    └── panels/
        ├── dashboard_panel.py      ← Live stat cards
        ├── orders_panel.py         ← Order list + create + filter
        ├── order_detail_dialog.py  ← Order detail, payments, status
        ├── patients_panel.py       ← Patient CRUD
        └── __init__.py
```

---

## Setup

```bash
# 1. Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Make sure your Django backend is running
#    Default: http://127.0.0.1:8000
#    Change BASE_URL in api_client.py if your server is elsewhere

# 4. Run the app
python main.py
```

---

## How the connection works

```
PySide6 Panel
    │
    ├── calls ApiClient method  (e.g. api.list_orders())
    │         │
    │         └── ApiWorker (QThread) runs call in background
    │                   │
    │                   └── requests.Session.get/post(...)
    │                               │
    │                               ▼
    │                       Django view receives request
    │                       → calls Service layer
    │                       → queries database
    │                       → returns JSON
    │                               │
    │                   worker.success.emit(dict)
    │                               │
    └── Panel slot receives dict → updates UI
```

Every API call runs on a **background thread** (ApiWorker).
This keeps the UI responsive while waiting for the server.
Results are delivered back to the UI thread via Qt signals,
which are thread-safe.

---

## Adding a new panel

1. Create `windows/panels/my_panel.py` with a class that extends `QWidget`
2. Add a `refresh()` method that calls the API
3. In `main_window.py`:
   - Import your panel
   - Add it to `self._panels` dict
   - Add a nav item tuple to `nav_items`

---

## Changing the server URL

Open `api_client.py` and update line 1:

```python
BASE_URL = "http://your-server-address/api"
```

---

## Adding a new API endpoint

Open `api_client.py` and add a method:

```python
def my_new_endpoint(self, param: int) -> dict:
    return self.get(f"my-endpoint/{param}/")
```

Then use it in any panel:

```python
w = ApiWorker(api.my_new_endpoint, param_value)
w.success.connect(self._on_data)
w.error.connect(self._on_error)
w.start()
```
