def palindrome(word):
    return word == word[::-1]
if __name__ == "__main__":
    text = input("enter a word:")
    if palindrome(text):
        print("palindrome")
    else:
        print("not palindrome")