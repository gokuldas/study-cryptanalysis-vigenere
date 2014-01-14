import matplotlib.pyplot as plt

from ctext import ctext
clen = len(ctext)

x, y = [], []

for i in range(1, 21): # i: possible key lengths
    match = 0
    for k in range(0, clen):
        if ctext[k] == ctext[(k + i) % clen]:
            match = match + 1
    x = x + [i]
    y = y + [match]

plt.stem(x, y)
plt.show()
