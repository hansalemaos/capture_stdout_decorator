# Captures stdout

```python
pip install capture-stdout-decorator
```

```python
from capture_stdout_decorator import print_capture
@print_capture
def hahaha():
    print("babab")
    return 4
@print_capture(print_output=False, return_func_val=False)
def hahaha2():
    print("babab")
    return 4
x = hahaha()
print(f'{x=}')
y = hahaha2()
print(f'{y=}')

# output:
babab
x=(4, 'babab\n')
y='babab\n'
		
```