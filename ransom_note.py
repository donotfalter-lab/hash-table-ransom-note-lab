def can_construct(ransomNote: str, magazine: str) -> bool:
    """
    Determines if ransomNote can be constructed using letters from magazine.
    Each letter in magazine can only be used once.

    Parameters:
        ransomNote (str): The target string to construct.
        magazine (str): The source string with available characters.

    Returns:
        bool: True if ransomNote can be constructed, False otherwise.
    """
    # Hash table mapping each character in the magazine to how many times it appears.
    counts = {}
    for char in magazine:
        counts[char] = counts.get(char, 0) + 1

    # Use up one occurrence per ransom note character; fail fast if it's missing or depleted.
    for char in ransomNote:
        if counts.get(char, 0) == 0:
            return False
        counts[char] -= 1

    return True
