def is_int_or_float(a, b=0):
    return (type(a) is int or type(a) is float and type(b) is int or type(b) is float)


def plus(a, b):
    if (is_int_or_float(a, b)):
        return a + b

    return None


def minus(a, b):
    if (is_int_or_float(a, b)):
        return a - b

    return None


def times(a, b):
    if (is_int_or_float(a, b)):
        return a * b

    return None


def division(a, b):
    if (is_int_or_float(a, b)):
        return a / b

    return None


def negation(a):
    if (is_int_or_float(a)):
        return -a

    return None


def power(a, b):
    if (is_int_or_float(a, b)):
        return a ** b

    return None


def remainder(a, b):
    if (is_int_or_float(a, b)):
        return a % b

    return None


print(plus(3, 2))
print(minus(3, 1))
print(times(2, 2))
print(division(9, 3))
print(negation(3))
print(power(10, 2))
print(remainder(3, 9))
