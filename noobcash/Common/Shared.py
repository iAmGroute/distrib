
import threading

class Shared:

    def __init__(self, obj, lockType=threading.RLock):
        self._obj  = obj
        self._lock = lockType()

    def __enter__(self):
        self._lock.__enter__()
        return self._obj

    def __exit__(self, exc_type=None, exc_value=None, traceback=None):
        self._lock.__exit__(exc_type, exc_value, traceback)

