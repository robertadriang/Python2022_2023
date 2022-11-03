# Write a module named utils.py that contains one function called process_item.
# The function will have one parameter, x, and will return the least prime number greater than x.
def is_prime(n):
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def process_item(x):
    if x < 2:
        return 2
    if x % 2 == 0:
        x += 1
    else:
        x += 2
    while True:
        if is_prime(x):
            return x
        else:
            x += 2

