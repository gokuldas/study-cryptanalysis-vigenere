from ctext import ctext
from substitute import *

keylen = 5
def alyz(keylen):
    for k in range(0, keylen):
        ct_sub = ctext[k::keylen]
        chrmap = {}
        for j in ct_sub:
            if j in list(chrmap):
                chrmap[j] = chrmap[j] + 1
            else:
                chrmap[j] = 1

        res = [[ky, v, diff(ky, 'E')] for ky, v in chrmap.items()]
        # format: ctext character, freq, possible k (wrt E)

        sortres = sorted(res, key = lambda x: x[1], reverse = True)
        print(sortres)
        print('\n')
