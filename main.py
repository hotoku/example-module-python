import mymodule


def main():
    print(mymodule.CONST)
    mymodule.CONST = 2
    print(mymodule.CONST)


if __name__ == "__main__":
    main()
