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

[Samy]: 1 and 2 
[Lalit]: 3 and 4

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

---

### Solution of exercise3_common_interests

The objective is to recommend friends and interests based on the similarity of user profiles.
We represent the data as a 2D matrix (User x Interest). We use **Cosine Similarity** to calculate the proximity between two users.
1. `cosine_similarity`: Computes the angle between two interest vectors. A value close to 1 indicates very similar tastes.
2. `get_similar_users`: Identifies the top K users with the highest similarity score.
3. `recommend_interests`: Uses the profiles of similar users to suggest interests that the target user has not yet rated (Collaborative Filtering).

### Solution of exercise4_mutual_followers

This exercise models a social graph using a **2D Boolean Adjacency Matrix**.
*   `matrix[i][j] = True` implies User `i` follows User `j`.
The class `FollowerMatrix` allows O(1) access to check a relationship but requires O(N) to retrieve all followers of a user.
We implement:
*   **Mutual Follows**: Detecting bidirectional edges (i -> j AND j -> i).
*   **Influence Score**: A metric based on the sum of followers and followings relative to the network size.

---

### Complexity analysis summary (continued)

### Complexity of exercise3_common_interests

**1. Time Complexity:**
*   To calculate similarity between 2 users, we check all `I` interests: **O(I)**.
*   To find the best matches for a user, we compare them against `U-1` other users.
*   Total complexity for one recommendation: **O(U * I)**.
*   Total complexity for all pairs (All-Pairs Similarity): **O(U^2 * I)**.

**2. Optimization for Sparse Matrices:**
Most users rate only a small subset of items. Instead of a full matrix, we can store data as a list of tuples `(interest_index, rating)`.
We then only iterate over the intersection of non-zero ratings, which significantly reduces the effective `I` to the average number of ratings `R_avg`.

**3. Space Complexity:**
*   **Full Matrix:** Stores `U * I` integers. **Space: O(U * I)**.
*   **Sparse Representation:** Stores only `R` total ratings. **Space: O(R)**.
*   If `R << U * I`, the sparse approach is much more memory efficient.

### Complexity of exercise4_mutual_followers

**1. Time Complexity:**
*   `Get_followers(j)`: Requires scanning the entire column `j`. **Complexity: O(N)**.
*   `Get_following(i)`: Requires scanning the entire row `i`. **Complexity: O(N)**.
*   `Is_following(i, j)`: Direct array access. **Complexity: O(1)**.

**2. Space Complexity:**
*   The adjacency matrix stores `N * N` booleans.
*   **Space: O(N^2)**.

**3. Scalability Limits:**
This representation becomes impractical when `N` is very large (e.g., millions of users).
*   For N = 1,000,000, we need 10^12 entries (Terabytes of RAM).
*   **Alternative:** For large graphs, **Adjacency Lists** (Hash Maps) are preferred as they only store existing edges, reducing space to **O(V + E)** (Vertices + Edges).