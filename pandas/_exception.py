
# try:
#   print(x)
# except NameError:
#   print("Variable x is not defined")
# except:
#   print("Something else went wrong")


try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print (type(inst))     # the exception instance
    print (inst.args)      # arguments stored in .args
    print (inst)         # __str__ allows args to be printed directly
    x, y = inst.args
    print(inst.args[1])
    print ('x =', x)
    print ('y =', y)

# <type 'exceptions.Exception'>
# ('spam', 'eggs')
# ('spam', 'eggs')
# x = spam
# y = eggs



