class Post:
    def __init__(self, post_id, user_id, content_preview, timestamp, likes, comments, shares):
        self.post_id = post_id
        self.user_id = user_id
        self.content_preview = content_preview
        self.timestamp = timestamp
        self.likes = likes
        self.comments = comments
        self.shares = shares
        # Compute engagement score: (likes * 1 + comments * 2 + shares * 3)
        self.engagement_score = (likes * 1) + (comments * 2) + (shares * 3)

    def __repr__(self):
        return f"Post{self.post_id}({self.engagement_score})"

# --- Part A: Maximum Engagement ---
def max_engagement(posts, left, right):
    if left == right:
        return posts[left]
    
    mid = (left + right) // 2
    max_left = max_engagement(posts, left, mid)
    max_right = max_engagement(posts, mid + 1, right)
    
    if max_left.engagement_score > max_right.engagement_score:
        return max_left
    else:
        return max_right

# --- Part B: Total and Average ---
def sum_engagement(posts, left, right):
    if left == right:
        return posts[left].engagement_score
    
    mid = (left + right) // 2
    return sum_engagement(posts, left, mid) + sum_engagement(posts, mid + 1, right)

def average_engagement(posts, left, right):
    if left > right:
        return 0
    total = sum_engagement(posts, left, right)
    count = right - left + 1
    return total / count

# --- Part C: Count by Threshold ---
def count_above_threshold(posts, left, right, threshold):
    if left == right:
        if posts[left].engagement_score > threshold:
            return 1
        else:
            return 0
            
    mid = (left + right) // 2
    left_count = count_above_threshold(posts, left, mid, threshold)
    right_count = count_above_threshold(posts, mid + 1, right, threshold)
    
    return left_count + right_count

# --- Part D: Merge Sort by Engagement (Descending) ---
def merge_sort_by_engagement(posts, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort_by_engagement(posts, left, mid)
        merge_sort_by_engagement(posts, mid + 1, right)
        merge(posts, left, mid, right)

def merge(posts, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid
    
    L = [0] * n1
    R = [0] * n2
    
    for i in range(n1):
        L[i] = posts[left + i]
    for j in range(n2):
        R[j] = posts[mid + 1 + j]
        
    i = 0
    j = 0
    k = left
    
    while i < n1 and j < n2:
        # Sort in Descending order (>=)
        if L[i].engagement_score >= R[j].engagement_score:
            posts[k] = L[i]
            i += 1
        else:
            posts[k] = R[j]
            j += 1
        k += 1
        
    while i < n1:
        posts[k] = L[i]
        i += 1
        k += 1
        
    while j < n2:
        posts[k] = R[j]
        j += 1
        k += 1

# --- Part E: Peak Hours Analysis ---
def find_peak_hour(likes, left, right):
    if left == right:
        return left
        
    mid = (left + right) // 2
    
    if likes[mid] > likes[mid + 1]:
        return find_peak_hour(likes, left, mid)
    else:
        return find_peak_hour(likes, mid + 1, right)


# ==========================================
# TEST CASES
# ==========================================

# 1. Initialize Posts (Engagement targets: 150, 320, 95, 280)
# Formula: (likes * 1) + (comments * 2) + (shares * 3)
p1 = Post(1, 101, "Preview 1", 1000, 150, 0, 0) # 150
p2 = Post(2, 102, "Preview 2", 1001, 320, 0, 0) # 320
p3 = Post(3, 103, "Preview 3", 1002, 95, 0, 0)  # 95
p4 = Post(4, 104, "Preview 4", 1003, 280, 0, 0) # 280

posts_array = [p1, p2, p3, p4]
n = len(posts_array)

print("--- Initial Posts Array ---")
print(posts_array)
print()

# Test Max Engagement
max_post = max_engagement(posts_array, 0, n - 1)
print(f"Max Engagement: {max_post} (Expected: Post2(320))")

# Test Sum and Average
total_eng = sum_engagement(posts_array, 0, n - 1)
print(f"Sum Engagement: {total_eng} (Expected: 845)")

avg_eng = average_engagement(posts_array, 0, n - 1)
print(f"Average Engagement: {avg_eng} (Expected: 211.25)")

# Test Count Above Threshold
threshold = 200
count_above = count_above_threshold(posts_array, 0, n - 1, threshold)
print(f"Count above {threshold}: {count_above} (Expected: 2 -> Post2, Post4)")

# Test Merge Sort (Descending)
print("\n--- Testing Merge Sort ---")
merge_sort_by_engagement(posts_array, 0, n - 1)
print(f"Sorted Posts: {posts_array}")
print("(Expected:[Post2(320), Post4(280), Post1(150), Post3(95)])")

# Test Peak Hour (Binary search style)
print("\n--- Testing Peak Hour ---")
hourly_likes =[5, 8, 12, 25, 30, 28, 15, 10]
peak_index = find_peak_hour(hourly_likes, 0, len(hourly_likes) - 1)
print(f"Hourly Likes: {hourly_likes}")
print(f"Peak Hour Index: {peak_index} -> {hourly_likes[peak_index]} likes (Expected: hour 4 -> 30 likes)")