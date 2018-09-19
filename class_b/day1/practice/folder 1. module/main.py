from module import Math
from module import PI
from module import sum as mysum

# from module import *
from matplotlib import pyplot as plt


if __name__ == "__main__":

    # 1. class
    math = Math()
    print(math.solv(3))

    # 2. variable
    print(PI)

    # 3. function
    print(sum(3, 5))
    print(div(5, 3))
