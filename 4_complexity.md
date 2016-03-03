# Time Complexity Cheat Sheet

1. We are trying to undetstand how your algorithm will perform
   under different loads (size of input).
1. The most important thing is the *shape* of your algorithm performance curve.
2. We generally only about the worst case, not the ideal case.


In order from best to worst:

Notation          Rule of thumb
----------        ------------------------------------------

O(1)              Simple expressions

O(log n)          Binary search, "divide-and-conquer", etc.

O(n)              One loop, linear search, etc.

O(n log n)        Most sorting algorithms

O(n^2)            Nested loops

O(2^n)            OMG
