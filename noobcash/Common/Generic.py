
def nop(*args, **kwargs):
    # pylint: disable=unused-argument
    pass

def identity(v):
    return v

def identityMany(*args):
    return args

def toTuple(thing):
    return thing if isinstance(thing, tuple) else (thing,)

def find(iterable, f):
    for item in iterable:
        if f(item):
            return item
    return None

def lowerFirst(name):
    return name[0].lower() + name[1:]

def listToBytes(aList, itemConverter):
    header  = len(aList).to_bytes(8, 'little')
    content = b''.join([itemConverter(item) for item in aList])
    return header + content
