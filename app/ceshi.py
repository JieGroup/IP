from abc import ABC, abstractmethod

# class A(ABC):

#     @classmethod
#     @abstractmethod
#     def ceshi(cls):
#         pass


# class B(A):

#     @classmethod
#     def ceshi(cls):
#         print('lihaine')
#         return

#     @classmethod
#     def wow(cls):
#         print('wudi')


# B.ceshi()
# B.wow()

a = {'a':{'b': 1, 'c':2}, 'b':{'b': 1, 'c':2}}

for key, val in a.items():
    print(f'key{key}')
    print(f'val{val}')