a = [(1,), (2,)]
a = str(a).replace('(', '').replace(',)', '')

print(eval(a))