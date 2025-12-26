# loops_and_iteration.py
# ----------------------------------------------------------
# MODULE: Loops & Iteration (For loops, While loops, Iterators)
# Author: Rudra Prasad Dutta
# Purpose: Explain loops and iteration in Python with examples,
#          common mistakes, DSA practice problems, and small tests.
# All human-readable explanations are provided as comments.
# ----------------------------------------------------------

# ----------------------------------------------------------
# 1) WHAT IS ITERATION?
# ----------------------------------------------------------
# Iteration means repeating a block of code multiple times,
# usually to process items in a sequence (list, string, range, etc.)
# Python provides two primary loop constructs:
#  - for loops (iterate over sequences/iterables)
#  - while loops (repeat while a condition holds)
#
# Python also supports iterator protocol, comprehensions, and generator expressions.

# ----------------------------------------------------------
# 2) FOR LOOPS (basic)
# ----------------------------------------------------------
# Syntax:
#   for variable in iterable:
#       # body
#
# The loop retrieves each element from the iterable and assigns it to 'variable'.
# Example: iterate over a list
fruits = ["apple", "banana", "cherry"]
for f in fruits:
    # here f is each element of the list in order
    # print is used for demonstration
    print("Fruit:", f)

# Iterate over characters in a string
for ch in "Python":
    print(ch, end=" ")
print()  # newline

# Using range() to iterate numeric sequences
# range(stop) -> 0..stop-1
# range(start, stop) -> start..stop-1
# range(start, stop, step) -> step increments
for i in range(3):         # 0,1,2
    print("i:", i)

for i in range(1, 6, 2):   # 1,3,5
    print("odd i:", i)

# ----------------------------------------------------------
# 3) WHILE LOOPS (basic)
# ----------------------------------------------------------
# Syntax:
#   while condition:
#       # body
#
# The body runs repeatedly while condition evaluates to True.
count = 0
while count < 3:
    print("count:", count)
    count += 1

# Important: ensure the loop's condition will eventually become False
# to avoid infinite loops.

# ----------------------------------------------------------
# 4) BREAK and CONTINUE
# ----------------------------------------------------------
# break -> exit the loop immediately
# continue -> skip to the next iteration
for x in range(10):
    if x == 5:
        break   # stops loop completely at x == 5
    if x % 2 == 0:
        continue  # skip even numbers (so only odd numbers get printed until break)
    print("odd <5:", x)

# ----------------------------------------------------------
# 5) ELSE CLAUSE ON LOOPS
# ----------------------------------------------------------
# Python supports an optional else block on loops:
#   for ...:
#       ...
#   else:
#       # runs if loop completed normally (no break)
#
# Useful for search loops to detect "not found" without a flag.
for x in [1, 2, 3]:
    if x == 10:
        print("found")
        break
else:
    print("Not found -> else executed because loop didn't break")

# while-else works similarly
i = 0
while i < 3:
    i += 1
    # no break here
else:
    print("while else executed (no break)")

# ----------------------------------------------------------
# 6) NESTED LOOPS
# ----------------------------------------------------------
# Loops can be nested; common for matrix operations or pairs.
matrix = [[1,2,3],[4,5,6],[7,8,9]]
for row in matrix:
    for val in row:
        print(val, end=" ")
    print()

# Complexity note: nested loops often produce O(n*m) behavior.

# ----------------------------------------------------------
# 7) ITERATORS & THE ITER PROTOCOL
# ----------------------------------------------------------
# Any object with __iter__() returning an iterator and iterator having __next__() is iterable.
# You can get an iterator with iter(), and manually fetch items with next().
lst = [10, 20, 30]
it = iter(lst)
print("next(it):", next(it))  # 10
print("next(it):", next(it))  # 20
# using next(it, default) prevents StopIteration exception
print("next(it, 'end'):", next(it, "end"))  # 30
print("next(it, 'end'):", next(it, "end"))  # 'end' since iterator exhausted

# ----------------------------------------------------------
# 8) ENUMERATE, ZIP, and REVERSED (useful iterator helpers)
# ----------------------------------------------------------
# enumerate(iterable, start=0) -> yields (index, value)
for idx, val in enumerate(["a","b","c"], start=1):
    print(idx, val)

# zip(*iterables) -> pairs items from iterables up to shortest length
for a, b in zip([1,2,3], ["x","y","z"]):
    print(a, b)

# reversed(seq) -> iterate sequence in reverse
for v in reversed([1,2,3]):
    print("rev:", v)

# ----------------------------------------------------------
# 9) LIST COMPREHENSIONS & GENERATORS (concise iteration)
# ----------------------------------------------------------
# List comprehension: [expr for var in iterable if condition]
squares = [x*x for x in range(5)]
print("squares:", squares)

# Generator expression (lazy): (expr for var in iterable)
gen = (x*x for x in range(5))
print("gen next:", next(gen))
# Generators don't build whole list in memory; good for large streams

# ----------------------------------------------------------
# 10) COMMON MISTAKES & GOTCHAS
# ----------------------------------------------------------
# 1) Modifying a list while iterating over it can skip elements.
#    Wrong:
#      for item in lst:
#          if cond(item):
#              lst.remove(item)
#    Better: iterate over a copy or build a new list.
#
# 2) Infinite loops with while (forgetting to update variables used in condition).
#
# 3) Off-by-one errors with range() — remember stop is exclusive.
#
# 4) Using break incorrectly in nested loops (break only exits inner loop).
#
# 5) Using mutable default arguments that are modified inside loops/functions.

# ----------------------------------------------------------
# 11) DSA PRACTICE PROBLEMS (with solutions & complexity)
# ----------------------------------------------------------
# Problem A: Sum of Elements
#   Given a list of numbers, return the sum.
#   Time: O(n), Space: O(1)
def sum_list(nums):
    total = 0
    for x in nums:
        total += x
    return total

# Problem B: Prefix Sums (build array of prefix sums)
#   Given nums, return array pref where pref[i] = sum(nums[:i+1])
#   Time: O(n), Space: O(n)
def prefix_sums(nums):
    pref = []
    running = 0
    for x in nums:
        running += x
        pref.append(running)
    return pref

# Problem C: Sliding Window Maximum (simple variant)
#   Given nums and window size k, return list of max for each window.
#   Naive approach (for learning): O(n*k); efficient approaches exist (deque) O(n).
def sliding_window_max_naive(nums, k):
    if k <= 0:
        return []
    n = len(nums)
    res = []
    for i in range(0, n - k + 1):
        window_max = nums[i]
        for j in range(i, i + k):
            if nums[j] > window_max:
                window_max = nums[j]
        res.append(window_max)
    return res

# Problem D: Detect cycle in list using Floyd's Tortoise and Hare (while loop)
#   Given a singly linked list defined by next pointers (simulated with dict mapping),
#   detect if there's a cycle. Uses iteration with two pointers. Time O(n), Space O(1).
#   For simplicity, we simulate list as dict: node -> next_node or None.
def detect_cycle(next_map, start):
    slow = start
    fast = start
    while True:
        if slow is None or fast is None:
            return False
        slow = next_map.get(slow)
        fast = next_map.get(fast)
        if fast is None:
            return False
        fast = next_map.get(fast)
        if slow == fast:
            return True

# Problem E: Remove duplicates while iterating (preserve order)
#   Given nums, return new list with first occurrence only.
#   Time: O(n), Space: O(n)
def remove_duplicates_preserve_order(nums):
    seen = set()
    out = []
    for x in nums:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out

# ----------------------------------------------------------
# 12) MINI TEST SUITE (assertions)
# ----------------------------------------------------------
def run_tests():
    print("\nRunning loop & iteration tests...")

    # sum_list
    assert sum_list([1,2,3,4]) == 10
    assert sum_list([]) == 0

    # prefix_sums
    assert prefix_sums([1,2,3]) == [1,3,6]

    # sliding_window_max_naive
    assert sliding_window_max_naive([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7]
    assert sliding_window_max_naive([1,2], 1) == [1,2]

    # detect_cycle: simulate nodes with dict mapping
    # Example: 1->2->3->4->2 (cycle)
    next_map_cycle = {1:2, 2:3, 3:4, 4:2}
    assert detect_cycle(next_map_cycle, 1) is True
    # Example: acyclic 1->2->3->None
    next_map_no = {1:2, 2:3, 3:None}
    assert detect_cycle(next_map_no, 1) is False

    # remove_duplicates_preserve_order
    assert remove_duplicates_preserve_order([1,2,2,3,1]) == [1,2,3]

    print("All loop & iteration tests passed ✔️")

# ----------------------------------------------------------
# 13) INTERVIEW / EXAM TIPS (short)
# ----------------------------------------------------------
# - Explain your loop choice: for vs while depend on whether you know iteration count.
# - Mention complexity explicitly (time/space).
# - For nested loops, explain how input sizes multiply (O(n*m) etc).
# - Avoid modifying the sequence you're iterating over; explain safer alternatives.
# - Use generator expressions for memory efficiency on large streams.
# - Show use of built-in helpers (enumerate, zip, reversed) to make code clearer.
# - For sliding-window problems show both naive and optimal ideas (deque).

# ----------------------------------------------------------
# 14) DEMO RUN (if executed directly)
# ----------------------------------------------------------
if __name__ == "__main__":
    print("=== Loops & Iteration Demo ===\n")
    # quick demo prints (first lines only to avoid large outputs)
    print("fruits example:", fruits)
    print("range example:", [i for i in range(3)])
    print("squares comprehension:", squares)

    # run tests
    run_tests()

# ----------------------------------------------------------
# END OF FILE
# ----------------------------------------------------------
