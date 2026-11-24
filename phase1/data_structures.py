"""
Data Structures in Python, for DSA
==================================

Run it top to bottom:  python3 phase1/data_structures.py
Read a section, run it, look at what it prints, then change something and run it again.

Sections
    1.  Where is .find()?  (JS array methods mapped to Python)
    2.  Comprehensions and generators (Python's map/filter)
    3.  enumerate, zip, sorting with key=
    4.  list internals: dynamic array, Big-O, copying, 2D grids
    5.  tuple: hashable, so it can be a dict key / set member
    6.  dict internals: hash table, ordering, safe access
    7.  set: O(1) membership (with a timing demo)
    8.  str: immutable, so build with a list + "".join()
    9.  collections: deque, defaultdict, Counter, OrderedDict
    10. heapq: priority queue / top-k
    11. bisect: binary search on a sorted list
    12. Stack patterns: valid brackets, monotonic stack
    13. Pitfalls that cost people DSA interviews

Big-O cheat sheet (average case, n = size)
    list   : x[i] O(1) | append/pop() O(1)* | insert(0,x)/pop(0) O(n) | x in list O(n) | sort O(n log n)
    dict   : d[k] get/set/del O(1) | k in d O(1)
    set    : add/remove O(1) | x in s O(1) | a & b O(min(len a, len b))
    deque  : append/appendleft/pop/popleft O(1) | dq[i] O(n) in the middle
    heapq  : heappush/heappop O(log n) | heap[0] peek O(1) | heapify O(n)
    bisect : search O(log n) | insort O(n) (the search is fast, the list shift isn't)
    str    : s[i] O(1) | s + t O(len s + len t) | x in s O(n*m) worst case
    (* = amortized: usually O(1), occasionally O(n) when the array grows)
"""

import copy
import time
from collections import deque, defaultdict, Counter, OrderedDict
import heapq
import bisect


def section(title):
    print()
    print("=" * 70)
    print(title)
    print("=" * 70)


users = [
    {"id": 1, "name": "Asha", "age": 31, "city": "Kolkata"},
    {"id": 2, "name": "Bikram", "age": 17, "city": "Pune"},
    {"id": 3, "name": "Chitra", "age": 24, "city": "Kolkata"},
    {"id": 4, "name": "Dev", "age": 17, "city": "Bengaluru"},
]


# =============================================================================
section("1. Where is .find()?")
# =============================================================================
"""
Python lists don't have methods like .find/.filter/.map. Python puts those
jobs in the LANGUAGE (for loops, comprehensions) and in BUILT-IN FUNCTIONS
(next, any, all, sum, max, sorted) that work on ANY iterable: list, tuple,
set, dict, string, file, generator. JS attaches methods to Array only, so
a JS Set has no .find(). In Python one next() works on all of them.

JS:     const u = users.find(u => u.id === 3);      // undefined if not found
"""


# Way 1: a plain loop with an early return. This is what .find() does inside.
def find_user(users, user_id):
    for u in users:
        if u["id"] == user_id:
            return u          # first match: leave the loop AND the function
    return None               # loop ran to the end: nothing matched


print("loop find      :", find_user(users, 3))
print("loop not found :", find_user(users, 99))

# Way 2: next() + a generator expression. The idiomatic one-line .find().
#
#   (u for u in users if u["id"] == 3)   <- generator: a LAZY sequence of matches.
#                                           Building it does no work at all.
#   next(generator, None)                <- pull the FIRST item out of it.
#                                           The generator scans only until it
#                                           finds one, then stops (like .find).
#                                           None is returned if it's empty.
found = next((u for u in users if u["id"] == 3), None)
missing = next((u for u in users if u["id"] == 99), None)
print("next() find    :", found)
print("next() missing :", missing)
# Without the default, an empty generator raises StopIteration. Always pass one.

# Way 3: for ... else (Python only). The else runs only if the loop did NOT break.
for u in users:
    if u["city"] == "Pune":
        print("for-else found :", u["name"])
        break
else:
    print("for-else       : nobody in Pune")

# .findIndex(): enumerate() gives (index, item) pairs.
idx = next((i for i, u in enumerate(users) if u["name"] == "Dev"), -1)
print("findIndex      :", idx)

# Careful: 3 different "find"s in Python
#   list.index(value)  -> index, but RAISES ValueError if missing (JS indexOf gives -1)
#   str.find(sub)      -> index or -1 (you used this in strings.py)
#   str.index(sub)     -> index, raises ValueError if missing
nums = [10, 20, 30]
print("list.index     :", nums.index(20))
print("value in list  :", 40 in nums, "(check this before .index to avoid the crash)")

"""
JS                                     Python
-------------------------------------  ------------------------------------------
arr.find(x => cond)                    next((x for x in arr if cond), None)
arr.findIndex(x => cond)               next((i for i, x in enumerate(arr) if cond), -1)
arr.filter(x => cond)                  [x for x in arr if cond]
arr.map(x => f(x))                     [f(x) for x in arr]
arr.some(x => cond)                    any(cond for x in arr)
arr.every(x => cond)                   all(cond for x in arr)
arr.reduce((a, b) => a + b, 0)         sum(arr)     (or functools.reduce)
arr.includes(x)                        x in arr
arr.indexOf(x)                         arr.index(x)       (raises if missing)
arr.forEach((x, i) => ...)             for i, x in enumerate(arr):
arr.sort((a, b) => a.age - b.age)      arr.sort(key=lambda u: u["age"])
[...arr] / arr.slice()                 arr[:]  or  arr.copy()
arr.push(x) / arr.pop()                arr.append(x) / arr.pop()
arr.shift() / arr.unshift(x)           dq.popleft() / dq.appendleft(x)   (deque!)
arr.length                             len(arr)
Math.max(...arr)                       max(arr)
arr.flat()                             [y for row in grid for y in row]
new Array(n).fill(0)                   [0] * n
Array.from({length: m}, () =>          [[0] * n for _ in range(m)]
    new Array(n).fill(0))
Object.entries(obj)                    d.items()
new Map() / new Set()                  dict / set
"""

print("filter adults  :", [u["name"] for u in users if u["age"] >= 18])
print("some minor?    :", any(u["age"] < 18 for u in users))
print("every adult?   :", all(u["age"] >= 18 for u in users))
print("total age      :", sum(u["age"] for u in users))
print("oldest         :", max(users, key=lambda u: u["age"])["name"])


# =============================================================================
section("2. Comprehensions and generators")
# =============================================================================
"""
A comprehension is a loop that BUILDS a collection, written inside the brackets.

    [expression  for item in iterable  if condition]

Reads left to right as: "give me expression, for each item, keeping only those
where condition is true". It's faster than append() in a loop (the loop runs
in C, and there's no .append method lookup on every step), and it's the
style every Python reviewer expects.
"""

squares = [n * n for n in range(6)]                      # list
evens = [n for n in range(10) if n % 2 == 0]             # list with filter
name_by_id = {u["id"]: u["name"] for u in users}         # dict comprehension
cities = {u["city"] for u in users}                      # set comprehension
labels = ["even" if n % 2 == 0 else "odd" for n in range(4)]  # if/else goes BEFORE for

print("squares   :", squares)
print("evens     :", evens)
print("name_by_id:", name_by_id)
print("cities    :", sorted(cities))
print("labels    :", labels)

# Nested: the for clauses read in the same order as nested loops would.
grid = [[1, 2, 3], [4, 5, 6]]
flat = [x for row in grid for x in row]        # for row in grid: for x in row: ...
transposed = [[row[c] for row in grid] for c in range(3)]
print("flat      :", flat)
print("transposed:", transposed)

"""
[ ... ] builds the whole list in memory NOW.
( ... ) builds a GENERATOR: it produces one value each time someone asks.

Use a generator when you only pass through the values once (sum, any, all,
max, next). sum(x*x for x in range(10_000_000)) uses almost no memory;
sum([x*x for x in range(10_000_000)]) builds an 80 MB list first.

A generator can be consumed only ONCE. After that it's empty.
"""
gen = (n * n for n in range(4))
print("first pass :", list(gen))
print("second pass:", list(gen), "<- already used up")


# =============================================================================
section("3. enumerate, zip, sorting with key=")
# =============================================================================

fruits = ["mango", "kiwi", "apple"]
prices = [120, 40, 90]

# enumerate: index + value together. Never write range(len(x)) just to get i.
for i, f in enumerate(fruits):
    print(f"{i}: {f}")

# zip: walk two (or more) lists side by side. Stops at the shortest one.
for f, p in zip(fruits, prices):
    print(f"{f:<6} Rs {p:>4}")
price_of = dict(zip(fruits, prices))
print("dict(zip) :", price_of)

"""
lambda is a one-expression anonymous function, like a JS arrow function:
    lambda u: u["age"]        ==   u => u.age

key= is NOT a comparator like JS's (a, b) => a - b. It's a function that turns
each item into the value to compare. Python calls it ONCE per item (n calls),
then sorts those values. JS calls the comparator O(n log n) times.

    list.sort()  sorts IN PLACE and returns None
    sorted(x)    returns a NEW list; works on any iterable (set, dict, str...)

Python's sort (Timsort) is STABLE: equal items keep their original order.
"""

print("by age          :", [u["name"] for u in sorted(users, key=lambda u: u["age"])])
print("by age desc     :", [u["name"] for u in sorted(users, key=lambda u: u["age"], reverse=True)])

# Sort by several keys at once: return a TUPLE. Tuples compare item by item.
# Age ascending, and for equal ages, name descending? Negate numbers to flip one key.
print("age, then name  :", [(u["age"], u["name"]) for u in sorted(users, key=lambda u: (u["age"], u["name"]))])
print("-age, then name :", [(u["age"], u["name"]) for u in sorted(users, key=lambda u: (-u["age"], u["name"]))])

words = ["bb", "a", "ccc", "dd"]
print("by length       :", sorted(words, key=len))   # any function works as key

broken = [3, 1, 2]
result = broken.sort()
print("x = arr.sort()  :", result, "<- classic bug, .sort() returns None")


# =============================================================================
section("4. list internals: dynamic array, Big-O, copying, 2D grids")
# =============================================================================
"""
A Python list is a DYNAMIC ARRAY of POINTERS (in C: PyObject **ob_item).
  - The list doesn't store your values. It stores addresses of objects that
    live elsewhere on the heap. That's why one list can hold mixed types.
  - x[i] is O(1): start address + i * 8 bytes.
  - append is amortized O(1): CPython over-allocates spare slots (about 1/8
    extra). When they run out, it allocates a bigger array and copies every
    pointer (O(n)), but that happens rarely enough that the AVERAGE stays O(1).
  - insert(0, x) and pop(0) are O(n): every pointer after the position shifts.
    Need a queue? Use deque (section 9), never list.pop(0).
  - x in list, .index(), .remove(), .count() are O(n): linear scans.
"""

import sys
lst = []
last_size = sys.getsizeof(lst)
print("len -> bytes allocated (watch it jump, not grow by 1 every time):")
for i in range(20):
    lst.append(i)
    size = sys.getsizeof(lst)
    if size != last_size:
        print(f"  len {len(lst):>2}: {size} bytes")
        last_size = size

"""
COPYING. Three different things that people mix up.
(Fix for your list.py note: `copy2_list = my_list` is NOT a deep copy. It's
not a copy at all. Both names point at the SAME list, which is why the ids
were equal.)

    b = a               ALIAS: same object, two names. JS: const b = a
    b = a.copy()/a[:]   SHALLOW copy: new outer list, SAME inner objects. JS: [...a]
    b = copy.deepcopy(a) DEEP copy: new everything, all the way down. JS: structuredClone(a)
"""
a = [[1, 2], [3, 4]]
alias = a
shallow = a.copy()
deep = copy.deepcopy(a)

a[0].append(99)        # mutate an INNER list
print("original:", a)
print("alias   :", alias, "  same object:", alias is a)
print("shallow :", shallow, "  <- inner list is shared, so it changed too")
print("deep    :", deep, "        <- fully independent")

"""
2D GRIDS: the #1 Python DSA bug.
    [[0] * 3] * 3  makes ONE inner list and puts 3 pointers to it in the outer list.
    [[0] * 3 for _ in range(3)]  runs [0]*3 three times: 3 separate lists.
([0] * 3 itself is fine, because ints are immutable. You never mutate a 0,
you replace it.)
"""
bad = [[0] * 3] * 3
bad[0][0] = 1
good = [[0] * 3 for _ in range(3)]
good[0][0] = 1
print("bad grid :", bad, " <- every row changed")
print("good grid:", good)

# Slicing makes a NEW list: O(k) time and memory for a k-length slice.
# Inside a recursive function, nums[1:] on every call turns O(n) into O(n^2).
# Pass indices (lo, hi) instead of slices in recursive DSA code.


# =============================================================================
section("5. tuple: hashable, so it can be a dict key / set member")
# =============================================================================
"""
Immutable means a tuple's hash can never change, so Python allows it as a dict
key and a set member. A list can't be one: if you mutated it after inserting,
its hash would change and the dict could never find it again.

This is everywhere in DSA:
  - grid coordinates in a visited set:    visited.add((row, col))
  - DP memo with several arguments:       memo[(i, j)] = ...
  - BFS state:                            (node, steps_left)
  - graph edges:                          edges = {(u, v), ...}

JS has no equivalent: a Set of [r, c] arrays compares by reference, so people
write `${r},${c}` strings. In Python, just use the tuple.
"""
visited = set()
visited.add((0, 1))
visited.add((2, 3))
print("(0, 1) visited?", (0, 1) in visited)

memo = {}
memo[(2, 3)] = 10
print("memo[(2, 3)] =", memo[(2, 3)], "  memo[2, 3] works too:", memo[2, 3])

try:
    {[1, 2]: "x"}
except TypeError as e:
    print("list as key   :", e)

# Tuples compare lexicographically: first items, then second items if tied...
# (Same rule makes the "due date as (y, m, d)" stretch goal in project.py work.)
print("(1, 9) < (2, 0):", (1, 9) < (2, 0))
print("(1, 2) < (1, 3):", (1, 2) < (1, 3))
print("(2026, 1, 5) < (2026, 12, 1):", (2026, 1, 5) < (2026, 12, 1))


# =============================================================================
section("6. dict internals: hash table, ordering, safe access")
# =============================================================================
"""
How d[key] is O(1):
  1. hash(key) turns the key into a big integer.
  2. That integer, masked to the table size, picks a slot index.
  3. If the slot is taken by a DIFFERENT key (a collision), CPython probes
     other slots in a pseudo-random sequence (open addressing) until it finds
     the key or an empty slot.
  4. The table is kept at most 2/3 full; past that it resizes (like list
     growth, amortized O(1)).

Since Python 3.7, dicts KEEP INSERTION ORDER. (Fix for your dict.py note:
"unordered" was true for old Python, not now.) CPython 3.6 made dicts
"compact": a small index table of slots points into a dense array of
(hash, key, value) entries kept in insertion order. Less memory, and ordered
iteration for free.

TS mapping: a dict is closer to `Map` than to a plain object. Keys can be
any hashable type (int, str, tuple, frozenset), not only strings.
"""

stock = {"apple": 5, "kiwi": 0}

print("d[k]           :", stock["apple"])
print("d.get(k)       :", stock.get("mango"), "<- None, no crash")
print("d.get(k, 0)    :", stock.get("mango", 0))
print("'kiwi' in d    :", "kiwi" in stock, "<- checks KEYS, O(1)")
print("0 in d.values():", 0 in stock.values(), "<- checks values, O(n)")

# Counting pattern. The plain-dict version. (Counter in section 9 does it for you.)
counts = {}
for ch in "banana":
    counts[ch] = counts.get(ch, 0) + 1
print("char counts    :", counts)

# Grouping pattern with setdefault: get the list, creating it if missing.
by_city = {}
for u in users:
    by_city.setdefault(u["city"], []).append(u["name"])
print("group by city  :", by_city)

# Iterate
for name, qty in stock.items():
    print(f"  {name}: {qty}")

# Never add/remove keys WHILE looping over the dict. Loop over a copy instead.
for k in list(stock):
    if stock[k] == 0:
        del stock[k]
print("after removing zero stock:", stock)

# Merge (3.9+): right side wins on duplicate keys, like {...a, ...b} in JS.
print("merge with |   :", {"a": 1, "b": 2} | {"b": 20, "c": 3})


# =============================================================================
section("7. set: O(1) membership (with a timing demo)")
# =============================================================================
"""
A set is a dict with keys and no values: same hash table, same O(1) lookup.
Rule for DSA: if you ask "have I seen x?" inside a loop, the thing you ask
must be a set or dict, never a list. A list makes that loop O(n^2).
"""

n = 100_000
as_list = list(range(n))
as_set = set(as_list)
lookups = 300

start = time.perf_counter()
for _ in range(lookups):
    (-1) in as_list          # worst case: scans all 100,000 items
list_time = time.perf_counter() - start

start = time.perf_counter()
for _ in range(lookups):
    (-1) in as_set           # one hash, one slot check
set_time = time.perf_counter() - start

print(f"{lookups} lookups in a list of {n}: {list_time * 1000:8.2f} ms")
print(f"{lookups} lookups in a set  of {n}: {set_time * 1000:8.2f} ms")
print(f"set is roughly {list_time / set_time:,.0f}x faster here")

# Dedupe while KEEPING order: dict.fromkeys (sets don't keep order).
print("dedupe, ordered:", list(dict.fromkeys([3, 1, 3, 2, 1])))

# frozenset: an immutable, hashable set, so it can go inside another set or be a key.
seen_pairs = {frozenset({"a", "b"})}
print("{b,a} seen?    :", frozenset({"b", "a"}) in seen_pairs)


# =============================================================================
section("8. str: immutable, so build with a list + ''.join()")
# =============================================================================
"""
Strings can't be changed in place. s += "x" creates a brand new string and
copies everything. In a loop that's O(n^2) in the worst case. (CPython
sometimes optimizes it in place, but don't rely on that; other Pythons don't.)

The fix: collect pieces in a list (O(1) append), then join once (O(n)).
"""
parts = []
for i in range(5):
    parts.append(str(i))
print("joined         :", "-".join(parts))

# Need to edit characters? Convert to a list, edit, join back.
chars = list("hello")
chars[0] = "j"
print("edited         :", "".join(chars))

# ord/chr: character <-> number. A 26-slot list is the fastest counter for a-z.
freq = [0] * 26
for ch in "abacus":
    freq[ord(ch) - ord("a")] += 1
print("a-z counts     :", {chr(i + ord("a")): c for i, c in enumerate(freq) if c})

print("isalnum/isalpha:", "a1".isalnum(), "a1".isalpha())
print("palindrome?    :", "racecar" == "racecar"[::-1])


# =============================================================================
section("9. collections: deque, defaultdict, Counter, OrderedDict")
# =============================================================================

# --- deque: double-ended queue, O(1) at BOTH ends -------------------------
"""
Implemented as a doubly linked list of fixed-size blocks (64 slots each), so
adding/removing at either end never shifts anything. This is your queue for
BFS. (JS has the same problem: arr.shift() is O(n).)
Trade-off: dq[i] in the middle is O(n). Use deque for ends, list for indexing.
"""
q = deque([1, 2, 3])
q.append(4)            # enqueue right
q.appendleft(0)        # push left
print("deque          :", q)
print("popleft        :", q.popleft(), "| pop:", q.pop(), "| now:", q)

# maxlen keeps only the last N items: a sliding window / recent history buffer.
# (AI engineering: "keep the last 3 chat turns" is exactly this.)
recent = deque(maxlen=3)
for msg in ["m1", "m2", "m3", "m4", "m5"]:
    recent.append(msg)
print("last 3         :", list(recent))

# BFS on a small graph: shortest number of hops from A.
graph = {"A": ["B", "C"], "B": ["D"], "C": ["D", "E"], "D": ["F"], "E": ["F"], "F": []}
dist = {"A": 0}
q = deque(["A"])
while q:
    node = q.popleft()
    for nxt in graph[node]:
        if nxt not in dist:             # dist doubles as the visited set
            dist[nxt] = dist[node] + 1
            q.append(nxt)
print("BFS hops from A:", dist)

# --- defaultdict: a dict that creates missing values for you ---------------
"""
defaultdict(list) calls list() to make a default the first time you touch a
missing key. No more setdefault or "if key not in d" checks.
Pitfall: even READING d[missing] inserts the key. Use `k in d` to test.
"""
adj = defaultdict(list)
edges = [(1, 2), (1, 3), (2, 3), (3, 4)]
for u, v in edges:          # undirected graph adjacency list
    adj[u].append(v)
    adj[v].append(u)
print("adjacency      :", dict(adj))

word_len_groups = defaultdict(set)
for w in ["hi", "yo", "cat", "dog", "hi"]:
    word_len_groups[len(w)].add(w)
print("group by length:", dict(word_len_groups))

# --- Counter: counting, done for you ----------------------------------------
"""
Counter is a dict subclass: element -> count. Missing keys read as 0 (and,
unlike defaultdict, reading doesn't insert them).
(AI engineering: token/word frequencies, label distributions in a dataset.)
"""
c = Counter("mississippi")
print("Counter        :", c)
print("c['s'], c['z'] :", c["s"], c["z"])
print("most_common(2) :", c.most_common(2))
print("anagram?       :", Counter("listen") == Counter("silent"))
print("c1 - c2        :", Counter("aabbc") - Counter("abd"), "<- keeps positives only")

# --- OrderedDict: a dict with move_to_end, the classic LRU cache tool ------
"""
Plain dicts are ordered now, but OrderedDict still has two things dict lacks:
  move_to_end(key)     O(1): mark as most recently used
  popitem(last=False)  O(1): evict the oldest
That's the whole LRU cache (LeetCode 146) in two calls.
"""
lru = OrderedDict()
capacity = 2
for key in ["a", "b", "a", "c"]:        # access a, b, a again, then c
    if key in lru:
        lru.move_to_end(key)
    else:
        lru[key] = key.upper()
        if len(lru) > capacity:
            evicted = lru.popitem(last=False)
            print("evicted        :", evicted)
print("LRU contents   :", list(lru))


# =============================================================================
section("10. heapq: priority queue / top-k")
# =============================================================================
"""
heapq is not a class. It's a set of functions that treat a plain list as a
binary MIN-heap. JS/TS has no built-in heap at all.

Array layout: for the item at index i,
    children are at 2*i + 1 and 2*i + 2, parent is at (i - 1) // 2.
Rule: every parent <= its children. So heap[0] is always the smallest.
The list is NOT fully sorted; only the parent/child rule holds.

    heappush(h, x)   add, then "sift up" past bigger parents     O(log n)
    heappop(h)       take heap[0], move last item to the top,
                     "sift down" below smaller children           O(log n)
    heapify(lst)     turn any list into a heap in place           O(n)
    h[0]             peek at the smallest                         O(1)
"""
h = []
for x in [5, 1, 8, 3, 2]:
    heapq.heappush(h, x)
print("heap list      :", h, "<- not sorted, but h[0] is the min")
print("pop order      :", [heapq.heappop(h) for _ in range(len(h))])

# Max-heap: Python only has min-heap. Push NEGATED numbers, negate on the way out.
mh = []
for x in [5, 1, 8, 3]:
    heapq.heappush(mh, -x)
print("max            :", -mh[0])

# (priority, item) tuples: compared by priority first, then by item if tied.
# If items can't be compared (dicts!), a tie crashes. Add a counter as tiebreaker.
tasks = []
order = 0
for prio, task in [(2, {"t": "write"}), (1, {"t": "plan"}), (2, {"t": "test"})]:
    heapq.heappush(tasks, (prio, order, task))
    order += 1
print("by priority    :", [heapq.heappop(tasks)[2]["t"] for _ in range(3)])

# Top-k largest: keep a MIN-heap of size k. Its top is the k-th largest so far.
# O(n log k), better than sorting O(n log n) when k is small.
# (AI engineering: "top-k most similar documents" in retrieval is this idea.)
scores = [40, 95, 12, 77, 88, 63, 99]
k = 3
top = []
for s in scores:
    heapq.heappush(top, s)
    if len(top) > k:
        heapq.heappop(top)             # throw away the smallest of the k+1
print("top 3 (heap)   :", sorted(top, reverse=True))
print("nlargest       :", heapq.nlargest(3, scores), "| nsmallest:", heapq.nsmallest(2, scores))


# =============================================================================
section("11. bisect: binary search on a sorted list")
# =============================================================================
"""
bisect_left(a, x)   first index where x could be inserted keeping a sorted
                    = index of the first element >= x
bisect_right(a, x)  index AFTER the last element <= x
                    = index of the first element > x
Both O(log n). Writing binary search by hand is error-prone; in Python you
reach for bisect unless the problem needs a custom search (like "binary search
on the answer", which you'll write by hand later).
"""
a = [10, 20, 20, 20, 30, 40]
print("bisect_left 20 :", bisect.bisect_left(a, 20))
print("bisect_right 20:", bisect.bisect_right(a, 20))
print("count of 20    :", bisect.bisect_right(a, 20) - bisect.bisect_left(a, 20))
print("items in [15, 35]:", bisect.bisect_right(a, 35) - bisect.bisect_left(a, 15))


def contains_sorted(arr, x):
    i = bisect.bisect_left(arr, x)
    return i < len(arr) and arr[i] == x


print("30 in a?       :", contains_sorted(a, 30), "| 25 in a?", contains_sorted(a, 25))

bisect.insort(a, 25)      # O(log n) to find the spot + O(n) to shift
print("after insort 25:", a)


# =============================================================================
section("12. Stack patterns: valid brackets, monotonic stack")
# =============================================================================
"""
A list IS a stack: append() to push, pop() to pop, stack[-1] to peek, all O(1).
"""


def is_valid_brackets(s):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for ch in s:
        if ch in pairs:
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
        else:
            stack.append(ch)
    return not stack            # empty list is falsy


print("'([]{})' valid?:", is_valid_brackets("([]{})"))
print("'([)]' valid?  :", is_valid_brackets("([)]"))

"""
MONOTONIC STACK: shows up in a lot of HARD problems (largest rectangle in
histogram, trapping rain water, daily temperatures, stock span).

Problem: for each number, find the next number to its right that's bigger.
Brute force: O(n^2). Monotonic stack: O(n).

Keep a stack of INDICES whose answer isn't known yet. Their values are
decreasing from bottom to top. When a bigger number arrives, it IS the answer
for every smaller value on top, so pop them and record it.
Each index is pushed once and popped once, so the total work is O(n).
"""


def next_greater(nums):
    ans = [-1] * len(nums)
    stack = []                         # indices, values decreasing
    for i, x in enumerate(nums):
        while stack and nums[stack[-1]] < x:
            ans[stack.pop()] = x
        stack.append(i)
    return ans


print("next greater   :", next_greater([2, 1, 5, 3, 4, 1]))


# =============================================================================
section("13. Pitfalls that cost people DSA interviews")
# =============================================================================

# 1) Floor division rounds toward NEGATIVE infinity. JS Math.trunc rounds toward 0.
print("-7 // 2        :", -7 // 2, "  (JS Math.trunc(-7/2) = -3)")
print("int(-7 / 2)    :", int(-7 / 2), "  <- truncation, if you need JS behaviour")
print("-7 % 3         :", -7 % 3, "  (JS -7 % 3 = -1)")

# 2) Integers never overflow. No Number.MAX_SAFE_INTEGER, no BigInt needed.
#    But problems that say "return the answer mod 10**9 + 7" still expect the mod.
print("2 ** 100       :", 2 ** 100)

# 3) Infinity for min/max initial values
best = float("inf")
for x in [7, 3, 9]:
    best = min(best, x)
print("min via inf    :", best)


# 4) Mutable default arguments are created ONCE, when the def runs.
def add_item_bad(item, bucket=[]):
    bucket.append(item)
    return bucket


def add_item_good(item, bucket=None):
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket


print("bad default    :", add_item_bad(1), add_item_bad(2), "<- the same list both times")
print("good default   :", add_item_good(1), add_item_good(2))

# 5) Recursion depth limit is about 1000. Deep DFS on a 10^5 node tree crashes
#    with RecursionError. Either convert to an explicit stack, or raise the limit:
#        sys.setrecursionlimit(10**6)
print("recursion limit:", sys.getrecursionlimit())

# 6) Removing from a list while looping over it skips items.
nums = [2, 2, 3, 4]
for x in nums:
    if x % 2 == 0:
        nums.remove(x)
print("remove in loop :", nums, "<- the second 2 was skipped: removing shifted it into the slot the loop already passed")
nums = [2, 2, 3, 4]
nums = [x for x in nums if x % 2 != 0]
print("comprehension  :", nums)

# 7) `is` vs `==`: `is` checks same object, `==` checks equal value.
#    Use `is` only for None (x is None). Never for numbers or strings.
print("[1] == [1]     :", [1] == [1], "| [1] is [1]:", [1] is [1])

print()
print("Done. Now open phase1/ds_exercises.py")
