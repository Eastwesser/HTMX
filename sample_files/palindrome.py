# palindrome.py


def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Normalize the string
    return s == s[::-1]  # Check if the string is equal to its reverse


if __name__ == "__main__":
    test_string = "A man a plan a canal Panama"
    if is_palindrome(test_string):
        print(f'"{test_string}" is a palindrome.')
    else:
        print(f'"{test_string}" is not a palindrome.')
