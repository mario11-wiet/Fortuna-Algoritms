import random
import time
import Voronoi as V

tab = []


def losowe(n):
    for i in range(n):
        x = random.randrange(-100, 100)
        y = random.randrange(-100, 100)
        tab.append((x, y))


losowe(100)
print(len(tab))
start = time.time()
vp = V.Voronoi(tab)
vp.process()
print(vp.get_output())

end = time.time()

print((end - start))
