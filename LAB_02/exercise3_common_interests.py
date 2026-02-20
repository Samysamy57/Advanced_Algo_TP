import math

def calculate_cosine_similarity(vec_a, vec_b):
    """
    Computes cosine similarity between two vectors of ratings.
    Range: [0, 1] for non-negative ratings.
    """
    if len(vec_a) != len(vec_b):
        return 0.0
    
    dot_product = 0
    norm_a = 0
    norm_b = 0
    
    for i in range(len(vec_a)):
        val_a = vec_a[i]
        val_b = vec_b[i]
        
        dot_product += val_a * val_b
        norm_a += val_a ** 2
        norm_b += val_b ** 2
        
    if norm_a == 0 or norm_b == 0:
        return 0.0
        
    return dot_product / (math.sqrt(norm_a) * math.sqrt(norm_b))

def get_similar_users(matrix, target_user_index, k=3):
    """
    Finds top K most similar users to target_user.
    Returns list of (user_index, similarity_score).
    """
    target_vec = matrix[target_user_index]
    scores = []
    
    for i in range(len(matrix)):
        if i == target_user_index:
            continue
            
        sim = calculate_cosine_similarity(target_vec, matrix[i])
        scores.append((i, sim))
        
    # Sort by similarity descending
    scores.sort(key=lambda x: x[1], reverse=True)
    
    return scores[:k]

def recommend_interests(matrix, target_user_index, k_neighbors=2):
    """
    Collaborative filtering: Recommend interests the user hasn't rated (0),
    based on what similar users liked.
    """
    target_vec = matrix[target_user_index]
    similar_users = get_similar_users(matrix, target_user_index, k_neighbors)
    
    num_interests = len(target_vec)
    recommendations = {} # interest_index -> weighted score
    
    for peer_idx, similarity in similar_users:
        peer_vec = matrix[peer_idx]
        
        for i in range(num_interests):
            # If target user hasn't rated this interest yet
            if target_vec[i] == 0:
                # Add peer's rating weighted by similarity
                if i not in recommendations:
                    recommendations[i] = 0
                recommendations[i] += peer_vec[i] * similarity
                
    # Sort recommendations by score
    sorted_recs = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)
    
    # Return top 3 interest indices
    return [idx for idx, score in sorted_recs][:3]

## Test set for edge cases
def test_recommendations():
    print("=== Edge cases: Friend Recommendation ===")
    
    # User-Interest Matrix (Rows: Users, Cols: Interests)
    # Interests: [Music, Sports, Tech, Fashion, Travel]
    matrix = [
        [10, 0, 8, 2, 5], # User 0: Likes Music, Tech
        [9, 1, 7, 3, 6],  # User 1: Similar to User 0
        [2, 9, 1, 8, 3],  # User 2: Likes Sports, Fashion (Different)
        [0, 0, 0, 0, 0],  # User 3: No activity
        [10, 0, 8, 2, 5], # User 4: Identical to User 0
    ]
    
    # Case 1: Similarity
    print(f"Similarity(0, 1): {calculate_cosine_similarity(matrix[0], matrix[1]):.2f} (High expected)")
    print(f"Similarity(0, 2): {calculate_cosine_similarity(matrix[0], matrix[2]):.2f} (Low expected)")
    print(f"Similarity(0, 4): {calculate_cosine_similarity(matrix[0], matrix[4]):.2f} (Identity)")
    
    # Case 2: Zero Vector
    print(f"Similarity(0, 3): {calculate_cosine_similarity(matrix[0], matrix[3]):.2f} (Zero expected)")
    
    # Case 3: Recommendations
    # User 0 hasn't rated 'Sports' (index 1). User 2 likes Sports.
    # But User 0 is not similar to User 2.
    # Let's see what logic recommends based on User 1.
    recs = recommend_interests(matrix, 0, k_neighbors=2)
    print(f"Recommendations for User 0: {recs}")

if __name__ == "__main__":
    test_recommendations()