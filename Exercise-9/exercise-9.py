def reverse(n) :
    
    num_string = str(n)

    #reverse the string using reversed method
    reversed_num = "".join(reversed(num_string))

    #output reversed number
    return reversed_num

def check_palindrome(number_):
    rev = reverse(number_)
    if rev == str(number_):
        print(f"Original number: {number_}")
        return("Yes. The given number is palindrome number.")

    else:
        print(f"Original number: {number_}")
        return("No. The given number is not palindrome number.")

print(check_palindrome(121))
print(check_palindrome(125))
