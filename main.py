import mymodule2
from mymodule import CONST, run


def main():
    run()  # 1
    CONST = 100
    run()  # 1 global CONST としても、やっぱり 1が出力される

    mymodule2.run()  # 2
    mymodule2.CONST = 200
    mymodule2.run()  # 200


if __name__ == "__main__":
    main()
