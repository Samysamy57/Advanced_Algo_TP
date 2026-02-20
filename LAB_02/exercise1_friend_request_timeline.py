def friend_request_timeline(message: str) -> str:
    n = len(message)
    
    upper_count = 0
    punct_count = 0
    alpha_count = 0
    
    repeat_count = 1
    max_repeat = 0
    
    # Single pass analysis
    for i in range(n):
        char = message[i]
        
        # Uppercase letters and alphabetic characters
        if char.isupper():
            upper_count += 1
            alpha_count += 1
        elif char.isalpha():
            alpha_count += 1
            
        # Count Punctuation
        if char == '!' or char == '?':
            punct_count += 1
            
        # Detect Repetition
        if i > 0:
            if char == message[i-1]:
                repeat_count += 1
            else:
                max_repeat = max(max_repeat, repeat_count)
                repeat_count = 1
                
    # Final check for repetition at the end of string
    max_repeat = max(max_repeat, repeat_count)
    
    # Check for SPAM
    if max_repeat > 3:
        return "SPAM DETECTED"
        
    # Calculate Ratio
    caps_ratio = 0.0
    if alpha_count > 0:
        caps_ratio = upper_count / alpha_count
        
    # Classify Message
    if caps_ratio >= 0.6 or punct_count >= 5:
        return "AGGRESSIVE"
    elif caps_ratio >= 0.3 or punct_count >= 3:
        return "URGENT"
    elif caps_ratio < 0.3 and punct_count < 3:
        return "CALM"
    else:
        # Fallback
        return "CALM"

## Test set for edge cases
def test_friend_request():
    print("=== Edge cases: Friend Request Timeline ===")
    
    cases = [
        ("Hey, want to connect?", "CALM"),           # Normal case
        ("PLEASE ACCEPT MY REQUEST!!!", "AGGRESSIVE"), # High caps + punct
        ("Are you free? I need to talk!!!", "URGENT"), # High punct
        ("heyyyyy", "SPAM DETECTED"),                # Repetition > 3
        ("", "CALM"),                                # Empty string
        ("noooo", "SPAM DETECTED"),                  # Repetition at end
        ("WHAT???", "AGGRESSIVE"),                   # High caps ratio (1.0)
        ("Hello!", "CALM")                           # Low caps, low punct
    ]
    
    for msg, expected in cases:
        result = friend_request_timeline(msg)
        print(f"Input: \"{msg}\"")
        print(f"Output: {result}")
        print(f"Expected: {expected}")
        
        if result == expected:
            print("test: successful")
        else:
            print("test: failed")
        print()

if __name__ == "__main__":
    test_friend_request()