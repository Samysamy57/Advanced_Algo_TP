def mutual_friends_detection(setA, setB):
    
    # 1. Intersection (Mutual Friends)
    # Using set intersection operation
    mutual_friends = set()
    for user in setA:
        if user in setB:
            mutual_friends.add(user)
            
    # 2. Difference (Unique to A)
    unique_A = set()
    for user in setA:
        if user not in setB:
            unique_A.add(user)
            
    # 3. Difference (Unique to B / Suggestions for A)
    unique_B = set()
    for user in setB:
        if user not in setA:
            unique_B.add(user)
            
    # 4. Union Calculation
    # Mathematical Union: A + B - Intersection (or sum of disjoint parts)
    union_size = len(mutual_friends) + len(unique_A) + len(unique_B)
    
    # 5. Jaccard Coefficient
    coefficient = 0.0
    if union_size > 0:
        coefficient = len(mutual_friends) / union_size
        
    # Print details as per requirement
    print(f"Mutual: {mutual_friends}")
    print(f"Jaccard: {coefficient:.2f}")
    
    # Return suggestions (Unique friends of B)
    return unique_B

## Test set for edge cases
def test_mutual_friends():
    print("=== Edge cases: Mutual Friends Detection ===")
    
    test_cases = [
        # Case 1: Overlap
        ({101, 102, 103, 104, 105}, {103, 104, 106, 107, 108}),
        # Case 2: Identical sets (Jaccard should be 1.0)
        ({1, 2}, {1, 2}),
        # Case 3: Disjoint sets (Jaccard should be 0.0)
        ({1, 2}, {3, 4}),
        # Case 4: Subset (A is inside B)
        ({1}, {1, 2, 3}),
        # Case 5: Empty sets
        (set(), set())
    ]
    
    for i, (setA, setB) in enumerate(test_cases):
        print(f"--- Test Case {i+1} ---")
        print(f"Set A: {setA}")
        print(f"Set B: {setB}")
        
        suggestions = mutual_friends_detection(setA, setB)
        
        print(f"Suggestions (Unique to B): {suggestions}")
        print()

if __name__ == "__main__":
    test_mutual_friends()