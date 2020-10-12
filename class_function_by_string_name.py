

import sys
# import string


def x_func():
    print('--> x_func')


class a_class:
    x = 10

    def __init__(self):
        self.a = 100

        print('__init__')

    def a_func(self):
        print('--->>> a_func')

    def a_func_2(self, x):
        print('--->>> a_func 222+'+str(x))


string_class_name = getattr(sys.modules[__name__], 'a_class')

# print(string_class_name.x)

# fn = getattr(string_class_name(), 'a_func_2')
# fn(12)

# string_class_name.a_func()

# string_func_name = getattr(sys.modules[__name__], 'x_func')()


# x = getattr(string_class_name, 'x')
# print(x)

# a = string_class_name.a
# print(a)


# lower = 'ToLower'

# print(lower.lower())


# import_type = 'IMPORT_SKU_IN_PLANOGRAM'
# import_type = 'IMPORT_PLANOGRAM_IN_STORE_TYPE'
# # import_type = 'IMPORT_PLANOGRAM_IN_REGION'
# import_type = import_type.replace('IMPORT_', '').split('_IN_')

# a, b = string.capwords(import_type[-1]), string.capwords(import_type[-2])

# # a ='fsfs_fsfs'
# if '_' in a:
#     temp = a.split('_')
#     a = temp[0] + string.capwords(temp[-1])
# print(a, b)
# # getattr()

# print('-'*20)
# z_ = a_class()
# z = getattr(a_class(), 'a_func_2')

# print(z.__name__)
