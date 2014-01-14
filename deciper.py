from ctext import ctext
from substitute import *

def decipher(vkey):
    ptext = ''
    keylen = len(vkey)
    for k in range(0, len(ctext)):
        ptext = ptext + diff(ctext[k], vkey[k % keylen])

    print(ptext, '\n')
    for i in range(0, len(ptext), keylen):
        if (i + keylen) > len(ptext):
            print(ptext[i:])
        else:
            print(ptext[i: i+keylen], end = ' ')
