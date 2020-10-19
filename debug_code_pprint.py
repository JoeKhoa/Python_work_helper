from pprint import pprint
from inspect import getmembers


class A:
    def __init__(self, test='test'):
        self.test = test
x = A()
# x.test = '1'


def var_dump(var, prefix=''):
    var_len = 1
    try:
        var_len = len(var)
    except:
        pass

    my_type = '[' + var.__class__.__name__ + \
        '(' + str(var_len) + ')]:'
    print(prefix, my_type, sep='')
    prefix += '    '
    for i in var:
        if type(i) in (list, tuple, dict, set):
            var_dump(i, prefix)
        else:
            if isinstance(var, dict):
                print(
                    prefix, i, ': (', var[i].__class__.__name__, ') ', var[i], sep='')
            else:
                print(prefix, '(', i.__class__.__name__, ') ', i, sep='')

# var_dump(x)
# pprint((x))

# pprint(vars(x))
vars(x)