class FollowerMatrix:
    def __init__(self, n_users):
        self.size = n_users
        self.actual_users = n_users
        # Initialize N x N matrix with False
        self.matrix = [[False for _ in range(n_users)] for _ in range(n_users)]

    def follow(self, follower, followee):
        """Set matrix[follower][followee] = True"""
        if 0 <= follower < self.size and 0 <= followee < self.size:
            self.matrix[follower][followee] = True

    def unfollow(self, follower, followee):
        """Set matrix[follower][followee] = False"""
        if 0 <= follower < self.size and 0 <= followee < self.size:
            self.matrix[follower][followee] = False

    def is_following(self, follower, followee):
        if 0 <= follower < self.size and 0 <= followee < self.size:
            return self.matrix[follower][followee]
        return False

    def get_followers(self, user):
        """Return list of users following 'user' (Column scan)"""
        followers = []
        for i in range(self.size):
            if self.matrix[i][user]:
                followers.append(i)
        return followers

    def get_following(self, user):
        """Return list of users 'user' follows (Row scan)"""
        following = []
        for j in range(self.size):
            if self.matrix[user][j]:
                following.append(j)
        return following

    def mutual_follow_detection(self):
        """Find all pairs (i, j) where i follows j AND j follows i"""
        mutuals = []
        # Iterate only upper triangle to avoid duplicates (i,j) and (j,i)
        for i in range(self.size):
            for j in range(i + 1, self.size):
                if self.matrix[i][j] and self.matrix[j][i]:
                    mutuals.append((i, j))
        return mutuals

    def influence_score(self, user):
        """(Followers + Following) / Total Users"""
        followers_count = len(self.get_followers(user))
        following_count = len(self.get_following(user))
        
        if self.actual_users == 0:
            return 0.0
            
        return (followers_count + following_count) / self.actual_users

## Test set for edge cases
def test_follower_matrix():
    print("=== Edge cases: Mutual Followers Matrix ===")
    
    # Initialize for 4 users (0, 1, 2, 3)
    fm = FollowerMatrix(4)
    
    # 0 follows 1, 1 follows 0 (Mutual)
    fm.follow(0, 1)
    fm.follow(1, 0)
    
    # 2 follows 0, 2 follows 1
    fm.follow(2, 0)
    fm.follow(2, 1)
    
    # 3 follows no one (Loner)
    
    print("Matrix State:")
    for row in fm.matrix:
        # Convert bool to T/F for display
        print(["T" if x else "F" for x in row])
        
    # Check Followers
    print(f"Followers of User 1 (should be 0, 2): {fm.get_followers(1)}")
    print(f"Following of User 2 (should be 0, 1): {fm.get_following(2)}")
    
    # Check Mutual
    print(f"Mutual pairs: {fm.mutual_follow_detection()}")
    
    # Check Influence
    # User 0: Follows 1 (1), Followed by 1, 2 (2) -> Total 3. Score 3/4 = 0.75
    print(f"Influence User 0: {fm.influence_score(0):.2f}")
    # User 3: 0/4 = 0.0
    print(f"Influence User 3: {fm.influence_score(3):.2f}")

    # Edge Case: Self follow (if allowed)
    fm.follow(3, 3)
    print(f"User 3 following self: {fm.is_following(3, 3)}")

if __name__ == "__main__":
    test_follower_matrix()