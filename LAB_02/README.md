## File Structure:
~~~
/LAB _02/
├── exercise1_friend_request_timeline.py
├── exercise2_mutual_friends.py
└── README.md (Team members and assigned exercises, Brief description of each solution, Complexity analysis summary)
~~~

---

## Team members and assigned exercises
Team: [12]

[Samy]: 1,2 
[Lalit]: 3,4

---

## Dependencies and Language version
Please use **python 3.11 or higher version**.

---

## Instructions

**Exercise 1 — Friend Request Timeline — Usage (Python)**

Input format:
* A string `message` representing the friend request content.

Output:
* A classification string: "CALM", "URGENT", "AGGRESSIVE", or "SPAM DETECTED".

**Exercise 2 — Mutual Friends Detection — Usage (Python)**

Input format:
* Two sets of integers `setA` and `setB` representing friend IDs for User A and User B.

Output:
* Returns the set of "Suggested Friends" (unique to B).
* Prints Mutual friends list and Jaccard similarity coefficient.

---

## Brief description of each solution

### Solution of exercise1_friend_request_timeline

The function `friend_request_timeline(message)` analyzes the sentiment of a message in a single pass. It iterates through the string to count uppercase letters, punctuation marks, and detects character repetitions (potential spam). 
Based on calculated ratios (Caps Ratio) and absolute counts (Punctuation), it classifies the message into categories (CALM, URGENT, AGGRESSIVE) or detects SPAM if characters are repeated excessively.

### Solution of exercise2_mutual_friends

The function `mutual_friends_detection(setA, setB)` implements fundamental set operations to analyze social connections.
1. **Intersection**: Identifies mutual friends.
2. **Difference**: Identifies friends unique to each user.
3. **Union**: Used to calculate the Jaccard similarity coefficient (`|Intersection| / |Union|`).
The function returns a list of suggested friends (friends of B that A does not know).

---

## Complexity analysis summary

### Complexity of exercise1_friend_request_timeline

For an n-character string, the algorithm performs a single pass loop.
Inside the loop, operations (comparisons, counter increments) are constant time O(1).
Therefore, the **time complexity is O(n)**.
The **space complexity is O(1)** because we only store a fixed number of integer counters regardless of the input size.

### Complexity of exercise2_mutual_friends

Let m be the size of setA and n be the size of setB.
Using Python's hash-based sets:
*   Intersection takes O(min(m, n)) on average.
*   Difference takes O(m) or O(n).
*   Union takes O(m + n).

The total **time complexity is O(m + n)**.
The **space complexity is O(m + n)** to store the resulting sets (mutual friends, union, suggestions).