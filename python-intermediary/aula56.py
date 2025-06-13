#count  um iterador sem fin
from itertools import count

cl = count()
rl = range(10)

print('cl', hasattr(cl, '__iter__'))
print('cl', hasattr(cl, '__next__'))
print('rl', hasattr(rl, '__iter__'))
print('rl', hasattr(rl, '__next__'))

for i in cl:
    if i > 100:
        break

print(i)
