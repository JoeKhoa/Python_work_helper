# class Foo:
#     def __init__(self):
#         print(self.__class__.__name__)

# class Coo(Foo):
#     def __init__(self):
#         print(self.__class__.__name__)

# X = Foo()

# Y = Coo()

class Mammal(object):
    def __init__(self, mammalName):
        print(mammalName, 'is a warm-blooded animal.')
        cls_name = self.__class__.__name__
        return cls_name

    def test_1(self):
        cls_name = self.__class__.__name__
        return cls_name

    @classmethod
    def test_2(cls, x):         
        print('test_2'+x)
 

class Dog_Cat(Mammal):
    def __init__(self):
        # print('Dog has four legs.')
        # print(self.__class__.__name__)
        super().__init__('x')


d1 = Dog_Cat()
a = d1.test_1()
d1.test_2(a)


# a = Dog_Cat.test_1()
# Dog_Cat.test_2(a)


# if "_" in "fsfs_fsf_":
#     print('found')


# a = 'f_sfs_fsf'

# a = a.split('_')
# a1, a2 =  a[-2],a[-1]
# print('a1, a2',a1, a2)

# print(['test', 'abc'] + ['1fsf'])


txt = 'AtestString'
print(txt.split('Atest'))
print(txt.replace('Atest', ''))