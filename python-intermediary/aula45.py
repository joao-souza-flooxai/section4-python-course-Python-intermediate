from sys import path

import aula45_package.modulo

from aula45_package import modulo

from aula45_package.modulo import *

from aula45_package.modulo import soma_do_modulo

# print(*path, sep="\n")

print(soma_do_modulo(1, 2))
print(aula45_package.modulo.soma_do_modulo(1, 2))
print(modulo.soma_do_modulo(1, 2))
