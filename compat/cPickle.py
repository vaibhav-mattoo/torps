import pickle as _pickle

HIGHEST_PROTOCOL = _pickle.HIGHEST_PROTOCOL

def dump(obj, file, protocol=None):
    return _pickle.dump(obj, file, protocol)

def load(file):
    return _pickle.load(file, encoding='latin1')

def dumps(obj, protocol=None):
    return _pickle.dumps(obj, protocol)

def loads(s):
    return _pickle.loads(s, encoding='latin1')
