# 6.Make an OrderedDict called fancy from the same pairs listed in 5 and print it. Did it print in the
# same order as plain?

from collections import OrderedDict
from Q5 import dct

fancy = OrderedDict(dct)

print(fancy)
