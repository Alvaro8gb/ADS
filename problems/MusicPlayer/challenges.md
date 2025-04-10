
# Challenges to adjust requirements

In Python it is not possible to perform the delete operation from the IPud in constant time O(1). As I take this exercise from C++ where this operation can be optimised. This page explains why.

 **Python's memory model** and **C++'s memory model** are different.
- `deque`** (or list) that allows element access by **pointer (iterator)** rather than by **index** in C++ enable access to element with random acess. 
- `list` in Python is not able to get the pointer of each element, elements are accesed by index (integers). That if you delete a element in the middle you can not track where it is as the index is pointing the other element. The element in position 2 can be change.


## 🧠 Conceptual Differences Between C++ and Python

### 🟦 In **C++**:
- ADS like `std::deque`, `std::vector`, and `std::list` store objects in memory in a way that gives you a **pointer** (or iterator) that actually references the **memory address** of the element.
- You can:
  - Dereference the pointer (`*it`) to access the element.
  - Increment the pointer (`++it`) to move to the next one.
  - Even store pointers or iterators, and they remain valid unless the container is modified in a way that invalidates them.

**Example (C++):**
```cpp
#include <deque>
#include <iostream>

int main() {
    std::deque<int> dq = {10, 20, 30, 40};
    auto it = dq.begin();
    ++it; // points to 20
    std::cout << *it << std::endl; // prints 20
}
```

### 🟨 In **Python**:
- You don't get raw memory pointers or true references to positions in ADS.
- Iterators in Python **don’t represent memory positions**, they are **stateful objects** that yield elements one-by-one.
- The iterator does **not give you back a reference to a "slot"** in the container. It only gives you the **value**, and then moves forward.

---

## ❌ Why You Can't Do This in Python

Let’s say you try to simulate what C++ does with an iterator pointing to an element, and then later use that "pointer" to remove or modify the element:

```python
data = [10, 20, 30, 40]
it = iter(data)
next(it)  # points to 10
next(it)  # "points" to 20

# Now let's say we want to delete that element (20), but we don't know the index
# Can we do something like *it = None? No.
```

Python's iterator **returns the value**, not a reference to a container position.


## 🔥 Key Technical Reasons Why Python Can’t Do This Like C++

| Feature                     | C++                             | Python                                |
|----------------------------|----------------------------------|----------------------------------------|
| Raw memory access          | Yes (`&`, `*`, pointer arithmetic) | No                                     |
| References to ADS slots | Yes (`iterator` is like a pointer) | No, `iterator` just yields values     |
| Control over layout        | Yes (`std::deque`, `std::vector`) | No, memory layout abstracted          |
| Pointer-based element access | Yes                             | No                                     |

---


## Conclusion

You can define IPud ADS using list.erase("song"), but knowing this have a time complexity of O(n)
