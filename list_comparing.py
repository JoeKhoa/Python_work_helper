# check if list are equal 
# using set()
a = ['x1','rr','e4','x3']
b = ['x1','rr','e4','x3']

# initializing list and convert into set object
# x = set(['x1','rr','x3','e4'])
# y = set(['x1','rr','e4','x3'])

# print ("List first: " + str(x))
# print ("List second: " + str(y))

# check if list x equals to y
# if x == y:
# if a == b:    
#     print("First and Second list are Equal")
# else:
#     print("First and Second list are Not Equal")



l1 = ['STT', 'Username', 'Mật khẩu', 'Tên', 'Role', 'Email', 'Số điện thoại', 'DoB', 'Trạng thái']

l2 = ['STT', 'Username', 'Mật khẩu', 'Tên', 'Role', 'Email', 'Số điện thoại', 'DoB', 'Trạng thái']

if l1 == l2:    
    print("First and Second list are Equal ++++++++ ")
else:
    print("First and Second list are Not Equal ------- ")


tx1 = 0
tx2 = 't----2'
print('or-> ', tx1 or tx2 )
print( tx1 and tx2 )

if tx1 or tx2:
    print('boolean')


print( '3 ngoi : ',tx1 if tx1 else tx2 )


string_start = '09125345ergdrgdr'
print(string_start.startswith('0'))
print(string_start.endswith('r'))

