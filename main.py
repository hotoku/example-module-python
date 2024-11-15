import mymodule
import mymodule2


def main():
    print(mymodule.CONST)  # 1
    mymodule.CONST = 2
    print(mymodule.CONST)  # 2

    print(mymodule2.CONST)  # 2
    mymodule2.CONST = 3
    print(mymodule2.CONST)  # 3
    mymodule2.run()  # 3


if __name__ == "__main__":
    main()
