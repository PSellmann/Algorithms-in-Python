def basicEuclid(a, b):
    r = a % b
    while r != 0:
        a = b
        b = r
        r = a%b
    return b

if __name__ == "__main__":
    print(basicEuclid(10, 5))