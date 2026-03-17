import time

class Post:
    def __init__(self, post_id, user_id, content, timestamp, likes, comments, shares):
        self.post_id = post_id
        self.user_id = user_id
        self.content = content
        self.timestamp = timestamp # Unix timestamp
        self.likes = likes
        self.comments = comments
        self.shares = shares
        self.engagement_score = self.calculate_score()
        self.next = None

    def calculate_score(self):
        return (self.likes * 1) + (self.comments * 2) + (self.shares * 3)

class EngagementPriorityQueue:
    def __init__(self):
        self.head = None
        self.size_count = 0

    def enqueue(self, new_post):
        # Recalculate score before inserting
        new_post.engagement_score = new_post.calculate_score()
        
        # If list is empty or new_post has the highest score
        if self.head is None or new_post.engagement_score > self.head.engagement_score:
            new_post.next = self.head
            self.head = new_post
        else:
            current = self.head
            # Traverse to find the correct position (descending order)
            while current.next is not None and current.next.engagement_score >= new_post.engagement_score:
                current = current.next
            
            new_post.next = current.next
            current.next = new_post
        
        self.size_count += 1

    def dequeue_max(self):
        if self.head is None:
            return None
        max_post = self.head
        self.head = self.head.next
        self.size_count -= 1
        max_post.next = None
        return max_post

    def peek_max(self):
        return self.head

    def update_score(self, post_id, n_likes, n_comments, n_shares):
        current = self.head
        prev = None
        
        # 1. Find and remove the node
        while current is not None and current.post_id != post_id:
            prev = current
            current = current.next
            
        if current is None:
            return # Post not found
            
        if prev is None:
            self.head = current.next
        else:
            prev.next = current.next
        self.size_count -= 1
        
        # 2. Update stats
        current.likes += n_likes
        current.comments += n_comments
        current.shares += n_shares
        
        # 3. Re-enqueue to maintain order
        self.enqueue(current)

    def get_top_k(self, k):
        result = []
        current = self.head
        count = 0
        while current is not None and count < k:
            result.append(current)
            current = current.next
            count += 1
        return result

    def decay_older_than(self, time_threshold, decay_percentage):
        temp_list = []
        # Extract all
        while self.head is not None:
            temp_list.append(self.dequeue_max())
            
        # Apply decay and re-insert
        for post in temp_list:
            if post.timestamp < time_threshold:
                # Apply decay (e.g. 20% decay means multiply by 0.8)
                post.likes = int(post.likes * (1.0 - decay_percentage))
                post.comments = int(post.comments * (1.0 - decay_percentage))
                post.shares = int(post.shares * (1.0 - decay_percentage))
            self.enqueue(post)

# --- Test Cases (T19 Style) ---

def test_priority_queue():
    pq = EngagementPriorityQueue()
    current_time = int(time.time())
    
    # Initial state
    p1 = Post(1, 10, "Post 1", current_time, 82, 0, 0) # Score 82
    p2 = Post(2, 11, "Post 2", current_time, 47, 0, 0) # Score 47
    p3 = Post(3, 12, "Post 3", current_time, 95, 0, 0) # Score 95
    p4 = Post(4, 13, "Post 4", current_time, 23, 0, 0) # Score 23

    pq.enqueue(p1)
    pq.enqueue(p2)
    pq.enqueue(p3)
    pq.enqueue(p4)

    print("Initial Queue (Top 4):")
    for p in pq.get_top_k(4):
        print(f"ID: {p.post_id}, Score: {p.engagement_score}")

    # Case: Update Post 2 with 10 likes
    print("\n--- Updating Post 2 (+10 likes) ---")
    pq.update_score(2, 10, 0, 0) # 47 + 10 = 57
    for p in pq.get_top_k(4):
        print(f"ID: {p.post_id}, Score: {p.engagement_score}")

    # Case: Decay older than current time
    print("\n--- Applying 20% Decay to older posts ---")
    pq.decay_older_than(current_time + 100, 0.2)
    for p in pq.get_top_k(4):
        print(f"ID: {p.post_id}, Score: {p.engagement_score}")

if __name__ == "__main__":
    test_priority_queue()