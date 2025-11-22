import time
import random
from bifurcated_sort import bfc_sort

# generate data
arr = [random.randint(0, 10**6) for _ in range(20000)]

# benchmark bfc_sort
copy1 = arr.copy()
start = time.time()
bfc_sort(copy1)
print("bfc_sort time:", time.time() - start)

# benchmark built-in sorted
copy2 = arr.copy()
start = time.time()
sorted(copy2)
print("sorted() time:", time.time() - start)


# Output :
# bfc_sort time: 0.026061058044433594
# sorted() time: 0.001425027847290039