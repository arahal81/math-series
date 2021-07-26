def fibonacci(n):
    if n < 0:
        return("You pass negative number")

    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        return fibonacci(n-1) + fibonacci(n-2)


def lucas(n):
    if n < 0:
        return("You pass negative number")

    if n == 0:
        return 2
    if n == 1:
        return 1
    if n > 1:
        return lucas(n-1) + lucas(n-2)


def sum_series(n, n_op1=0, n_op2=1):
    if n < 0:
        return("You pass negative number")
    if n == 0:
        return n_op1
    if n == 1:
        return n_op2
    else:
        return sum_series(n-1, n_op1, n_op2) + sum_series(n-2, n_op1, n_op2)


# print(lucas())
# print(fibonacci(1))
print(sum_series(10, 4, 7))
