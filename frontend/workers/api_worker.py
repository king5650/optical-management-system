"""
workers/api_worker.py — Background thread for API calls

WHY THREADS?
────────────
If you call the API directly on the main (UI) thread, the window freezes
while waiting for the server to respond. QThread moves the API call to a
background thread so the UI stays responsive. The result is delivered back
to the UI thread via Qt signals (which are thread-safe).

USAGE PATTERN (in any panel):
    worker = ApiWorker(api.list_orders)
    worker.success.connect(self._on_orders_loaded)
    worker.error.connect(self._on_error)
    worker.start()
"""

from PySide6.QtCore import QThread, Signal


class ApiWorker(QThread):
    """
    Runs any callable in a background thread.
    Emits 'success' with the result dict, or 'error' with a string message.
    """
    success = Signal(object)   # emits the dict/list returned by the API call
    error   = Signal(str)      # emits the error message string

    def __init__(self, fn, *args, **kwargs):
        """
        fn      — the api_client method to call (e.g. api.list_orders)
        args    — positional arguments to pass to fn
        kwargs  — keyword arguments to pass to fn
        """
        super().__init__()
        self._fn = fn
        self._args = args
        self._kwargs = kwargs

    def run(self):
        """Called automatically by QThread.start() in the background."""
        try:
            result = self._fn(*self._args, **self._kwargs)
            self.success.emit(result)
        except Exception as e:
            self.error.emit(str(e))
