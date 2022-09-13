def retrocontador(e):
    print("{},".format(e), end="")
    if e > 0:
        retrocontador(e-1)

retrocontador(10)

print()

"""def sumatorio(e):
    print("{},".format(e),end="")

    if e < 10:
        sumatorio(e+1)

sumatorio(0)
"""

    