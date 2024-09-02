#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1
    a = 10
    b = 5
    result = add(a, b)
    print("{} + {} = {}".format(a, b, result))
    result = sub(a, b)
    print(f"{} - {} = {}".format(a, b, result))
    result = mul(a, b)
    print(f"{} * {} = {}".format(a, b, result))
    result = div(a, b)
    print(f"{} / {} = {}".format(a, b, result))
