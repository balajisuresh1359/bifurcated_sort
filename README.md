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
from bifurcated_sort import bfc_sort

arr = [15, 3, 8, 1, 12, 6]
bfc_sort(arr)

print(arr)
# Output: [1, 3, 6, 8, 12, 15]
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

## License

MIT License