import time
import random
import Voronoi as V

tab = []


def losowe(n):
    for i in range(n):
        x = random.randrange(-100, 100)
        y = random.randrange(-100, 100)
        tab.append((x, y))


losowe(1000)
print(len(tab))
start = time.time()
vp = V.Voronoi(tab)
vp.process()
end = time.time()

print((end - start))
