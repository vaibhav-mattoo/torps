import builtins

builtins.xrange = range
builtins.unicode = str

_original_filter = builtins.filter
def _list_filter(*args):
    return list(_original_filter(*args))
builtins.filter = _list_filter
