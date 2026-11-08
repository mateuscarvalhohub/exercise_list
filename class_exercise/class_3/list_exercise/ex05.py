"""
Exercise 05

Goal:
Analyze candidate pools for different job positions
using set operations.

Concepts Practiced:
- Sets
- Set operations
- Intersection
- Union
- Difference
- Data analysis

Tests:
✓ Common candidates ({'Caio'})
✓ All unique candidates ({'Ana', 'Bruno', 'Caio', 'Duda', 'Elena'})
✓ Python Developer only ({'Ana', 'Bruno'})
"""

python_dev_vacancy = {"Ana", "Bruno", "Caio"}
analist_vacancy = {"Caio", "Duda", "Elena"}

print(python_dev_vacancy & analist_vacancy)
print(python_dev_vacancy | analist_vacancy)
print(python_dev_vacancy - analist_vacancy)
