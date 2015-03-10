def memoize(f):
    def _wrapped(*args, **kwargs):
            key = repr((args, kwargs))
            if key in _wrapped._cache:
                return _wrapped._cache[key]
            else:
                value = f(*args, **kwargs)
                _wrapped._cache[key] = value
                return value
    _wrapped._cache = {}
    _wrapped.__name__ = f.__name__
    _wrapped.__doc__ = f.__doc__
    return _wrapped
