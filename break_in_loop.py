
in_activate_obj = ['a', 'b', 'c']


for item in in_activate_obj:
    print(item)
    if item == 'b':
        exist_obj = item
        break
    else:
        exist_obj = None
    
print(exist_obj)