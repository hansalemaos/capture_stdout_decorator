import sys
from functools import wraps
from io import StringIO


def print_capture(f_py=None, print_output=True, return_func_val=True):

    assert callable(f_py) or f_py is None

    def _decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            vala = None
            stdout = sys.stdout
            sys.stdout = file = StringIO()
            try:
                vala=func(*args, **kwargs)
            finally:
                sys.stdout = stdout

            rea = file.getvalue()
            if print_output:
                print(rea)
            if return_func_val:
                return vala, rea
            else:
                return rea

        return wrapper

    return _decorator(f_py) if callable(f_py) else _decorator


