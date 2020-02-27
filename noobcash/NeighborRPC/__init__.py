
import importlib

__all__ = [
    'GetLatestBlockID',
]

def lowerFirst(name):
    return name[0].lower() + name[1:]

modules  = [importlib.import_module('.' + name, __name__) for name    in __all__]
handlers = {m.CMD: m                                      for m       in modules}
requests = {lowerFirst(name): m.request                   for name, m in zip(__all__, modules)}
