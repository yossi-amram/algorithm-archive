

def is_palindrome(number_string):
    if len(number_string) in [0, 1]:
        return True
    if number_string[0] == number_string[-1]:
        return is_palindrome(number_string[1:-1])
    return False


# returns the largest palindrome that's a product of two k-digit numbers
def largest_product_palindrome(k):
    max_product = 0
    start = 10 ** (k - 1)
    end = start * 10
    for i in range(start, end):
        for j in range(start, i + 1):
            product = i * j
            if product > max_product:
                if is_palindrome(str(product)):
                    max_product = product
    return max_product




print(largest_product_palindrome(5))
