def remove_chars(word, n):
    print(f"Original string: {word}")
    remaining_chars = word[n:]
    return remaining_chars

print(remove_chars("pynative", 4))
print(remove_chars("pynative", 2))
