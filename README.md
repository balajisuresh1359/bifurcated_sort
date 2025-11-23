# bifurcated_sort

A hybrid sorting algorithm that splits the input into two linked lists (ascending and descending), processes non-fitting elements using a BST-assisted insertion strategy, and merges both lists to produce the final sorted output.

📄 Full documentation and detailed walkthrough:  
https://balajisuresh1359.github.io/balaji-area/code/bifurcated_insertion_sort.html

---

## Installation
```bash
pip install bifurcated_sort
```

---

## Example Usage
```python
from bifurcated_sort import bfc_sort, bfc_sorted

# In-place sorting
arr = [15, 3, 8, 1, 12, 6]
bfc_sort(arr)
print(arr)
# Output: [1, 3, 6, 8, 12, 15]

# Return a new reversed sorted list (does not modify the original)
result = bfc_sort([5, 2, 8], inplace=False, reverse=True)
result
# Output: [8, 5, 2]

# Using bfc_sorted (always returns a new list)
arr2 = [2, 1, 32]
result = bfc_sorted(arr2)
result
# Output: [1, 2, 32]   # inplace=False by default

arr2
# Output: [2, 1, 32]   # original list remains unchanged
```

---

## Benchmark (20,000 random integers)
```python
# Output:
# bfc_sort time: 0.026061058044433594
# sorted() time: 0.001425027847290039
```

---


## Complexity

- **Time Complexity**: 
  - Best case: O(n)
  - Average case: O(n log n) to O(n√n)
  - Worst case: O(n²)
- **Space Complexity**: O(n)

---


## Bifurcated Sort Demo


https://github.com/user-attachments/assets/f1f1f229-28d2-4216-b46a-09800d637bae



## License

MIT License
